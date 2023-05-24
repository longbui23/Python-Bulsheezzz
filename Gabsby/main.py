#Christine and Long

#import packages
from gadsbyFunx import*

#int var
text = open('gadsby.txt')
list = text.readlines()
gadCharDict = freq_dict(list, 184, 5861)

#call func
new_dict = alp_perc_dict(gadCharDict)

for word in new_dict:
	print(word)

text.close()
