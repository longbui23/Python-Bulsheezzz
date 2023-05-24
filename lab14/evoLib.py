#import packages
from random import*


#int var
gAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '


#create func
def makeIndiv(size, alp):
	'''return a string containing an individual of the correct size composed of characters randomly chosen from the alphabet'''

	#int var
	newStr = ''

	#loop to add char into new string
	for i in range(size):
		newStr += alp[randint(0,len(alp)-1)]

	#output
	return newStr


def evalFit(ind_str, targ_str):
	'''counts and returns the number of char in its 2 param that match'''

	#guardians
	assert len(ind_str) == len(targ_str), '2 string must be equal size'
	
	#int var
	count = 0

	#for loop to check similar characters
	for i in range(len(ind_str)):
		if ind_str[i] == targ_str[i]:
			count += 1

	#output
	return count


def crossover(par1, par2):
	'''makes two Strings representing parents and produces a new string representing the offspring'''

	#guardians
	assert len(par1) == len(par2), '2 genes must have the same length to crossover'

	#crossover
	ran_pt = randint(0, len(par1))
	offspr = par1[:ran_pt] + par2[ran_pt:]

	#output
	return offspr


def mutate(ind, alp):
	'''randomly chooses a character in the individual to be replaced by a random character from the alphabet'''

	#int var
	mut_gene = ''
	
	#mutating process
	pos = randint(0, len(ind)-1)
	mut_gen = ind[:pos] + alp[randint(0, len(alp)-1)] + ind[pos+1:]
	
	#output
	return mut_gen


def repro(par1, par2, num, alp):
	'''return offspring produced by crossover and mutation operation'''

	#guardians
	assert len(par1) == len(par2), '2 genes must have the same length to crossover'

	#production process
	#crossover
	offspr = crossover(par1, par2)
	#mutate
	for i in range (num):
		offspr = mutate(offspr, alp)

	#output
	return offspr


def makePop(num_ind, size_ind, alp):
	'''create the initial population for the genetic algorithm'''

	#int var
	pop =[]

	#loop to generate individuals for population
	for i in range(num_ind):
		gen = [makeIndiv(size_ind, alp), 0]
		pop.append(gen)

	#output
	return pop


def mapFit(pop, tar_str):
	'''compute fitness of an individual'''

	for i in range(len(pop)):
		pop[i][1] = evalFit(pop[i][0], tar_str)


def pickDNA(pop):
	'''comparing the 2 parents and pick the one that has higher fitness'''

	#int var
	par1 = choice(pop)
	par2 = choice(pop)

	#while loop to choose again if par1 is the same as par2
	while pop.index(par1) == pop.index(par2):
		par2 = choice(pop)

	#return the gene
	if par1[1] >= par2[1]:
		return par1[0]
	else:
		return par2[0]


def getFittest(pop):
	'''return a sub-list of individual that has the highest fitness from a population'''

	#int var
	fittest = pop[0]
	
	#return the fittest
	for i in range(len(pop)):
		if pop[i][1] > fittest[1]:
			fittest = pop[i]

	#output
	return fittest

