'''
Clean up the txt file to make processing more efficient.
Not for MC, but for word counting and stuff.

@authors: Adam (apata68) & Nico (NicoDiLullo)
'''

import numpy as np
import matplotlib.pyplot as plt

#open file, set to read mode, text file
file = open("Desktop/QR22/pd_IQR22/tweetsAsText.txt", "r")
#read contents
contents = file.read()
#close file because life
file.close()
#put everything in lower case
#~11,000 number of unique instances reduction!!!!!!!
contents = contents.lower()
#write to file
f = open("Desktop/QR22/pd_IQR22/testFile.txt", "x")
f.write(contents)
f.close()
#this all works ^^

#split at punctuation

#more testing
#change keyword
f = open("Desktop/QR22/pd_IQR22/testFile.txt")
contents = f.read()
contents.replace('"', " ")
contents.replace(".", " ")
contents.replace(",", " ")
contents.replace("!", " ")
contents.replace("&amp", " ")
contents.replace("...", " ")
contents.replace("\n", "")
contents.replace("  ", " ")
contents.replace("   ", " ")
f.close()
f = open("Desktop/QR22/pd_IQR22/testFile.txt", "w")
f.write(contents)
f.close()

#below code reduces iterations to ~50000
'''
f = open("Desktop/QR22/pd_IQR22/testFile.txt")
contents = f.read()
contents.replace('"', " ")
contents.replace(".", " ")
contents.replace(",", " ")
contents.replace("!", " ")
contents.replace("&amp", " ")
contents.replace("...", " ")
contents.replace("\n", "")
contents.replace("  ", " ")
contents.replace("   ", " ")
f.close()
f = open("Desktop/QR22/pd_IQR22/testFile.txt", "w")
f.write(contents)
f.close()
contents
content
contents
type(contents)
len(contents)
contents.replace('\n',' ')
contents.replace('"',' ')
contents.replace('”',' ')
contents.replace('.',' ')
contents.replace(',',' ')
c = contents.replace(',',' ')
c = c.replace('\n',' ')
c
c = c.replace('”',' ')
c = c.replace('"',' ')
c
c = c.replace('.',' ')
c = c.replace(',',' ')
c
c = c.replace('  ',' ')
c
c = c.replace('  ',' ')
c
c = c.replace('&amp','and')
c
c = c.replace('“',' ')
c
c = c.replace('  ',' ')
c
c = c.replace(';',' ')
c = c.replace('!',' ')
c
'''