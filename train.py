import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import nps_chat

import pandas as pd

path = "rawDataset_combined.csv"
list = []

with open(path) as f:
    df = pd.read_csv(f, header=None)
    """
    df[2] = df[2].str.replace("&#39;", "'")
    df[2] = df[2].str.replace("&quot;", '"')
    df[2] = df[2].str.replace(r"\s\\\sR", "")
    df[2] = df[2].str.replace(r"\s\\\sr", "")
    """
    col = df[1]
    for row in col:
        # print(row)
        list.append(str(row))
    # print(list)
    raw = "\n".join(list)
    # print(type(raw))
    # print(raw)
    # print(type(col))
    """
    raw = list(col)
    print(raw)
    print(type(raw))
    """
    # raw = str(col)
    # print(raw)
    # print(type(raw))
    tokens = word_tokenize(raw)
    # print(tokens)
    words = [w.lower() for w in tokens]
    # print(words)
    vocab = sorted(set(words))
    # print(vocab)


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.wordnet.words())
    english_vocab2 = set(w.lower() for w in nltk.corpus.nps_chat.words())
    english_vocab3 = set(w.lower() for w in nltk.corpus.brown.words())
    english_vocab5 = set(w.lower() for w in nltk.corpus.webtext.words())
    english_vocab6 = set(w.lower() for w in nltk.corpus.words.words())
    unusual = (
        text_vocab
        - english_vocab
        - english_vocab2
        - english_vocab3
        - english_vocab5
        - english_vocab6
    )
    return sorted(unusual)


print(len(unusual_words(vocab)))

s = pd.Series(unusual_words(vocab))
s.to_csv("unusual.csv", header=False)
