import csv
import sys
import nltk

fname = "res/all-the-news/articles2.csv"
csvfile = open(fname, "r")
csv.field_size_limit(sys.maxsize)
dico = dict()

try:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    for row in reader:
        tokens = nltk.word_tokenize(row[9])
        tagged = nltk.pos_tag(tokens)
        for token in tagged:
            if token[1] == "NN":
                if token[0] in dico.keys():
                    dico[token[0]] += 1
                else:
                    dico[token[0]] = 1
        print(dico)

finally:
    csvfile.close()

