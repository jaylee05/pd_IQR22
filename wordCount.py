'''
What does this code do?

@authors: apata68 & NicoDiLullo

last modified: 13.02.2023
'''
import numpy as np
import matplotlib.pyplot as plt

#get an array of every word in data set
words = []
f = open('testFile.txt')
#need to make the whole file the same case for analysis on this end...

for word in f.read().split():
    words.append(word)

#right now all this does nothing because all words are technically unique

#bruh

#make into set
words_as_set = set(words)
#back into a list, because sets are not subscriptable
word_set_as_list = list(words_as_set)
#how many times does each word in the set occur
counts = []
for i in range(len(word_set_as_list)):
    counts.append(words.count(word_set_as_list[i]))
#plot its