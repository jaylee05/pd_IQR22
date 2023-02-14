'''
Clean up the txt file to make processing more efficient.
Not for MC, but for word counting and stuff.

@authors: Adam (apata68) & Nico (NicoDiLullo)
'''

import numpy as np
import matplotlib.pyplot as plt

#open file, set to read mode, text file
file = open("Desktop/QR22/pd_IQR22/tweetsAsText.txt", "r", "t")
#read contents
contents = file.read()
#close file because life
file.close()
#put everything in lower case
contents = contents.lower()
#write to file
f = open("testFile.txt", "x")
f.write(contents)
f.close()