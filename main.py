import nltk

from nltk.book import *

""" condordance view """

text1.concordance("whale")
text2.concordance("love")
text3.concordance("god")
text4.concordance("seoul")
text5.concordance("fuck")

""" similar """

text1.similar("whale")
text2.similar("love")
text3.similar("god")
text4.similar("seoul")
text5.similar("fuck")

""" common_contexts """

text1.common_contexts(["whale", "pony"])
text2.common_contexts(["love", "sin"])
text3.common_contexts(["god", "devil"])
text4.common_contexts(["seoul", "Newyork"])
text5.common_contexts(["fuck", "help"])

""" dispersion plot """

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

""" generate (deprecated in nltk3.0) """

text1.generate()
text2.generate()
text3.generate()
text4.generate()
text5.generate()

""" frequent distribution """

fdist1 = FreqDist(text1)
fdist1.most_common(50)
fdist1["whale"]
fdist1.plot(50, cumulative=True)
fdist1.hapaxes()  # the words that occur once only, the so-called hapaxes

""" fine-grained selection of words """

fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

""" Collocations and Bigrams """

# A collocation is a sequence of words that occur together unusually often. Thus red wine is a collocation, whereas the wine is not.
# To get a handle on collocations, we start off by extracting from a text a list of word pairs, also known as bigrams.

list(bigrams(["more", "is", "said", "than", "done"]))

# Now, collocations are essentially just frequent bigrams, except that we want to pay more attention to the cases that involve rare words.
# In particular, we want to find bigrams that occur more often than we would expect based on the frequency of the individual words. The collocations() function does this for us.

text4.collocations()
text8.collocations()

# The collocations that emerge are very specific to the genre of the texts.