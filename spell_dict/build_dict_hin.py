from spellchecker import SpellChecker

spell = SpellChecker(language=None, case_sensitive=False)


spell.word_frequency.load_text_file('hincorpus.txt',encoding='utf-8')

spell.export('my_hin.gz', gzipped=True)
