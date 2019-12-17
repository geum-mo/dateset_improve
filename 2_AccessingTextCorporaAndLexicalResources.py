import nltk

""" Corpus #1: Gutenberg """

nltk.corpus.gutenberg.fileids()

emma = nltk.corpus.gutenberg.words("austen-emma.txt")
len(emma)

""" If you want to do something learnt from 1_LanguageProcessingAndPython, do it in a way below """

emma = nltk.Text(nltk.corpus.gutenberg.words("austen-emma.txt"))
emma.concordance("surprize")

""" For simplicity """

from nltk.corpus import gutenberg

gutenberg.fileids()
emma = gutenberg.words("austen-emma.txt")

""" """
from nltk.corpus import gutenberg

gutenberg.fileids()
emma = gutenberg.words("austen-emma.txt")

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))  # raw()
    num_words = len(gutenberg.words(fileid))  # words()
    num_sents = len(gutenberg.sents(fileid))  # sents()
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(
        round(num_chars / num_words),
        round(num_words / num_sents),
        round(num_words / num_vocab),
        fileid,
    )

# corpus > text > sentence > word (corpora > texts > sentences > words)

macbeth_sentences = gutenberg.sents("shakespeare-macbeth.txt")
macbeth_sentences

macbeth_sentences[1116]

longest_len = max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s) == longest_len]


""" Web and Chat Text """

# The corpus is organized into 15 files,
# where each file contains several hundred posts collected on a given date, for an age-specific chatroom (teens, 20s, 30s, 40s, plus a generic adults chatroom).
# The filename contains the date, chatroom, and number of posts; e.g., 10-19-20s_706posts.xml contains 706 posts gathered from the 20s chat room on 10/19/2006.

from nltk.corpus import nps_chat

chatroom = nps_chat.posts("10-19-20s_706posts.xml")
chatroom[123]


""" Brown Corpus """

# The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University.
# This corpus contains text from 500 sources, and the sources have been categorized by genre,
# such as news, editorial, and so on. 1.1 gives an example of each genre (for a complete list,
# see http://icame.uib.no/brown/bcm-los.html).

from nltk.corpus import brown

brown.categories()

brown.words(categories="news")

brown.words(fileids=["cg22"])
brown.sents(categories=["news", "editorial", "reviews"])

from nltk.corpus import brown

news_text = brown.words(categories="news")
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ["can", "could", "may", "might", "must", "will"]
for m in modals:
    print(m + ":", fdist[m], end=" ")

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)
genres = ["news", "religion", "hobbies", "science_fiction", "romance", "humor"]
modals = ["can", "could", "may", "might", "must", "will"]
cfd.tabulate(conditions=genres, samples=modals)
