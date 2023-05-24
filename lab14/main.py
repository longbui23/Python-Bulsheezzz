#long and christine
#import packages
from evoLib import*
from random import*

#call func
pop = makePop(5, 6, 'ABC')


test_pop = [['ABC BA', 4], ['CA CAB', 2], ['B ABBB', 1], ['AA CAC', 3]] 
assert getFittest(test_pop)==['ABC BA', 4], 'Incorrect fittest individual'

test_pop[1][1] = 5
assert getFittest(test_pop)==['CA CAB', 5], 'Incorrect fittest individual' 

test_pop[3][1] = 6
assert getFittest(test_pop)==['AA CAC', 6], 'Incorrect fittest individual' 
print('Success!')