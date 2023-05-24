def addDigsums(num):
	'''calculate the digitSum of 2 digits number'''

	#guardians
	assert isinstance(num, int), 'number must be an integer'
	assert 0 <= num <= 99, 'number must in between 1 and 99'

	#body
	digSum = num // 10 + num % 10

	#recursive loops
	if num == 0:
		return 0
	else:
		totalDigSums = digSum + addDigsums(num - 1)
		return totalDigSums

#call func
print(addDigsums(10))