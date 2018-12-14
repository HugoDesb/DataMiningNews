import csv
import sys
import nltk

fname = "res/all-the-news/articles2.csv"
csvfile = open(fname, "r")
csv.field_size_limit(sys.maxsize)

try:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    for row in reader:
        tokens = nltk.word_tokenize(row[9])
        tagged = nltk.pos_tag(tokens)
        for token in tagged:
            if token[1] == "NN":
                print(token[0])
finally:
    csvfile.close()

