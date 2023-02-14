'''
Clean up the txt file to make processing more efficient.

@authors: Adam (apata68) & Nico (NicoDiLullo)
'''

import numpy as np
import matplotlib.pyplot as plt

file = open("Desktop/QR22/pd_IQR22/tweetsAsText.txt", "r")
contents = file.read()
file.close()
