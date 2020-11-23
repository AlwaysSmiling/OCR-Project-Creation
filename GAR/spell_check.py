from spellchecker import SpellChecker
import io


with io.open('raw_output.txt', 'r', encoding='utf-8') as c:
    content = c.read()

content_list = content.split()
correct_list = []


spell = SpellChecker()

for words in content_list:
    if spell.known([words]):
        correct_list.append(words)
    else:
        correct_list.append(spell.correction(words))


with io.open('checked_output.txt', 'w', encoding='utf-8') as f:
    for word in correct_list:
        word = word.lower()
        f.write(word + ' ')




    
