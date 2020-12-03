import cv2
import pytesseract
import io
import os
import sys
from docx import Document
from spellchecker import SpellChecker
from itertools import zip_longest


class SourceImg:
    def __init__(self):
        self.srcimg = cv2.imread("source.png")
        self.edit = self.srcimg

    def get_gray_noise(self):
        self.edit = cv2.cvtColor(self.edit, cv2.COLOR_BGR2GRAY)
        self.edit = cv2.threshold(
            self.edit, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]


lanstr = str(sys.argv[1])
out = str(sys.argv[2])
img = SourceImg()
img.get_gray_noise()
if out == "pdf":
    pdf = pytesseract.image_to_pdf_or_hocr(img.srcimg, lang=lanstr, extension="pdf")
    with io.open("final.pdf", "w+b") as k:
        k.write(pdf)
    os._exit(0)
raw = pytesseract.image_to_string(img.edit, lang=lanstr)
content_list = raw.split()
correct_list = []
if lanstr == "hin":
    spell = SpellChecker(local_dictionary="./spell_dict/my_hin.gz")
    for words in content_list:
        if spell.known([words]):
            correct_list.append(words)
        else:
            correct_list.append(spell.correction(words))
    with io.open("final_output.txt", "w", encoding="utf-8") as f:
        for word in correct_list:
            word = word.lower()
            f.write(word + " ")
    if out == "txt":
        os._exit(0)

elif lanstr == "eng":
    spell = SpellChecker()
    for words in content_list:
        if spell.known([words]):
            correct_list.append(words)
        else:
            correct_list.append(spell.correction(words))
    with io.open("final_output.txt", "w", encoding="utf-8") as f:
        for word in correct_list:
            word = word.lower()
            f.write(word + " ")
    if out == "txt":
        os._exit(0)

else:
    print("ERROR-- wrong language input")
with io.open("final_output.txt", "r", encoding="utf-8") as r:
    final_text = r.read()
raw_list = list(raw)
for i in range(len(raw_list) - 1):
    if raw_list[i] == " " and raw_list[i + 1] == " ":
        raw_list.pop(i + 1)
finl_list = list(final_text)
end_list = []
for i, j in zip_longest(raw_list, finl_list, fillvalue=" "):
    if str(i) != "\n":
        end_list.append(j)
    elif str(i) == "\n":
        if str(j) == " ":
            end_list.append(i)
        else:
            end_list.append(j)
            end_list.append(i)
finish = "".join(end_list)
docu = Document()
docu.add_paragraph(finish)
docu.save("final_doc.docx")
