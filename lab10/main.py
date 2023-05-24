# Long and Maggie
#Fork this repl.
# Your main code goes here.

#import packages
from functions import *
import numpy as np
import matplotlib as plt

#int var
count = 0
error = []

#open file
inFile = open("validation.txt")
rev = inFile.readline()

while rev:
	error.append(abs(getSentRate(rev) - textSent(rev)))
	rev = inFile.readline()

#plotting
n, bins, patches = plt.hist(error, 4, normed=1, facecolor='blue', alpha=0.5)
plt.xlabel('Error')
plt.ylabel('Frequency')
plt.title('Histogram for errors of computer rating system compared to actual human rating')
plt.show()

#opt3:
#suggested improvements: connections between positive and negative words. For example: if not + fabulous--> negative instead of not (-1) + fabulous(+2) result in positive(+1) sentiment.
	