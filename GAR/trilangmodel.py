from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict


langmodel = defaultdict(lambda: defaultdict(lambda: 0))


for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1
 

for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count



