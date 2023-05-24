#Christine and Long
from evoLib import *
from numpy import *
from matplotlib import *

# ==== Main Program Below ====
#lists for drawing line plot
gen = []
fit_index_per = []


sonnetStr = "Shall I compare thee to a summers day".upper()
sonnetSize = len(sonnetStr)
numMuts = int(sonnetSize * 0.05)


pop = makePop(200, sonnetSize, gAlpha)
mapFit(pop, sonnetStr)
best = getFittest(pop)
print('0 : ' + best[0])

generation = 0
while best[0] != sonnetStr:

	newPop = [best]
	for individual in range(len(pop)):
		parent1 = pickDNA(pop)
		parent2 = pickDNA(pop)
		offspring = repro(parent1, parent2, numMuts, gAlpha)
		newPop.append([offspring, 0])
        
	pop = newPop
	generation = generation + 1
	gen.append(generation)
	
	mapFit(pop, sonnetStr)
	best = getFittest(pop)
	fit_index_per.append(best[1])
	print(str(generation) + ': ' + best[0])

#plot
# plot(gen, fit_index_per)
# xlab('generation')
# ylab('fittest index')
# title('Line graph of fittest level according to generation')
# show()


