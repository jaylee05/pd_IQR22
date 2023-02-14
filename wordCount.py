'''
What does this code do?

@authors: apata68 & NicoDiLullo

last modified: 13.02.2023
'''
import numpy as np
import matplotlib.pyplot as plt

#get an array of every word in data set
words = []
f = open('trumpTweets.txt')
for word in f.read().split():
    words.append(word)
#make into set
words_as_set = set(words)

#do some more stuff

#plot its