# Your functions go here
def getSentRate(txtStr):
	'''receiving the review + rating and return the rating'''

	#int var
	rat = int(txtStr[0])

	#output
	return rat


def getRevText(txtStr):
	'''receiving the review + rating and return the review in the review'''

	#int var
	rev = txtStr.lstrip(txtStr[0])

	#output
	return rev


def cleanText(txt):
	'''lower case all leters, remove all spaces from beginning or end, and remove all non-alphabetic and non-space characters'''

	#int var
	newStr = ''
	
	#cleaning process
	txt = txt.lower()                 		#lowercase all letters
	txt = txt.strip()       	         	#removing all space

	#while to check and exclude non-alphabet letters
	for char in txt:
		if char.isalpha() or char.isspace():
			newStr = newStr + char
	
	#output
	return newStr


def wordSent(txt):
	'''find word inside the text and return the average rating according to the word'''
	
	#int var
	txt = cleanText(txt)

	#open file
	inFile = open("training.txt")
	line = inFile.readline()
	skip = cleanText(open('skip.txt').readline())
	totalAvg = 0
	count = 0

	#while loop to calculate total average rating
	while line:
		if txt in cleanText(line) and txt not in skip.split():   #cannot split line because some word has different form(Ex: the word fabulous sometimes be written as fabulousness in the review of training.txt)
			totalAvg = totalAvg + getSentRate(line)
			count += 1
		line = inFile.readline()

	#Output: conditional for word does not appear
	if totalAvg == 0:
		return 0
	#return the average rating
	else:
		avg = totalAvg / count
		return avg


def textSent(wordStr):
	'''takes a String of multiple words as an argument and computes the sentiment of the entire text as the average sentiment rating of all of its words. '''

	#int var and split string to process in for loop
	wordStr = cleanText(wordStr).split()
	totalRat = 0
	count = 0

	#loop to increment totalRating based on per word input
	for word in wordStr:
		if wordSent(word) != 0:
			totalRat = totalRat + wordSent(word)
			count += 1

	#calculate the average sentimentrating
	if totalRat == 0:
		return 0
	else:
		aveSen = totalRat/ count
		return aveSen

