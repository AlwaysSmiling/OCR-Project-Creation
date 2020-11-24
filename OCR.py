import cv2 
import pytesseract
import io
import os
import sys
from spellchecker import SpellChecker


class SourceImg:
    def __init__(self):
        self.srcimg = cv2.imread("source_raw.jpg")
        self.edit = self.srcimg

    def get_gray_noise(self):
        self.edit = cv2.cvtColor(self.edit, cv2.COLOR_BGR2GRAY)
        self.edit = cv2.medianBlur(self.edit, 3)


lanstr = str(sys.argv[1])
out = str(sys.argv[2])


img = SourceImg()

img.get_gray_noise()

if out == 'pdf':
    pdf = pytesseract.image_to_pdf_or_hocr(img.srcimg,lang=lanstr, extension='pdf')
    with io.open('final.pdf', 'w+b') as k:
        k.write(pdf)
    os._exit(0)

raw = pytesseract.image_to_string(img.edit,lang=lanstr) 

with io.open('raw_output.txt', "w", encoding="utf-8") as f:
    f.write(raw)


with io.open('raw_output.txt', 'r', encoding='utf-8') as c:
    content = c.read()

content_list = content.split()
correct_list = []

if lanstr == 'hin':
    
    spell = SpellChecker(local_dictionary='./spell_dict/my_hin.gz')

    for words in content_list:
        if spell.known([words]):
            correct_list.append(words)
        else:
            correct_list.append(spell.correction(words))


    with io.open('final_output.txt', 'w', encoding='utf-8') as f:
        for word in correct_list:
            word = word.lower()
            f.write(word + ' ')
    if out == 'txt':
        os._exit(0)

elif lanstr == 'eng':

    spell = SpellChecker()

    for words in content_list:
        if spell.known([words]):
            correct_list.append(words)
        else:
            correct_list.append(spell.correction(words))


    with io.open('final_output.txt', 'w', encoding='utf-8') as f:
        for word in correct_list:
            word = word.lower()
            f.write(word + ' ')
    if out == 'txt':
        os._exit(0)

else:
    print('ERROR-- wrong language input')
    






































    

