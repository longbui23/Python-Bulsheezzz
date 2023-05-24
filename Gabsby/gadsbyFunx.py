#Christine and Long


#define functions
def first_let(strList, start, end):
	'''print every first letter of the text in a defined range'''

	#loop for line
	for i in range(start-1, end):
		line = strList[i][0]
		line = line.lower()
		print(line)


def freq_dict(strList, start, end):
	'''return the frequency of characters in Gadsby'''

	#create a frequency dictionary
	freq_dict = dict()

	#loop to check the number of character appears
	for line in strList[start-1:end + 1]:
		line = line.lower()
		#loop to check characters in a line
		for char in line:
			if char not in freq_dict:
				freq_dict[char] = 1
			else:
				freq_dict[char] += 1	

	#output
	return freq_dict


def sumChars(word_dict):
	'''return the total number of characters in the text'''

	#int var
	total_sum = 0

	#loop to increment number of characters
	for word in word_dict.keys():
		total_sum += word_dict[word]

	#output
	return total_sum


def perc_dict(word_dict):
	'''return a dictionary of percentage of a certain character from the total number of character'''

	#int var
	tot_char = sumChars(word_dict)
	perc_dict = dict()

	#percentage
	for word in word_dict.keys():
		perc_dict[word] = (word_dict[word]/tot_char) * 100

	#output
	return perc_dict


def alp_perc_dict(word_dict):
	''' takes a character dictionary as an argument and returns a new dictionary of letters – that is, only the alphabetic (i.e. a-z) characters -- from the original dictionary'''
	
	#Int var
	new_word_dict = dict()

	#loop to filter un-alpha characters
	for word in word_dict.keys():
		if word.isalpha():
			new_word_dict[word] = word_dict[word]

	#percentage dictionary creation + sorting it
	new_perc_dict = perc_dict(new_word_dict)
	new_perc_dict_ord = sorted(new_perc_dict.items(), key=lambda x:x[1], reverse=True) 
	
	#output
	return new_perc_dict_ord


def cleanLines(strList):
	'''clean the lines from unecessary letters'''

	#int var
	newList = ''

	#cleaning process
	newList = strList.strip(" ").strip('\n')

	#Output
	return newList