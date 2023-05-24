#import packages
from simmod import*
import numpy
from matplotlib.pyplot import *
from random import*

#defining function
def getYears():
	'''return the list of number of years from 2000 to 2100'''
	years = numpy.loadtxt("results/rcp2.6.csv", usecols =(2), delimiter =',', skiprows = 1, unpack = True)
	return years


def deltatemp(rcp):
	'''return the list of change in temperature for each scenario requested'''

	#guardians
	assert rcp == 2.6 or rcp == 4.5 or rcp == 6.0 or rcp == 8.5, 'Must choose a valid RCP!'

	#documentation
	t_s = numpy.loadtxt("results/rcp"+str(rcp)+".csv", usecols =(30), delimiter =',', skiprows = 1, unpack = True)
	return t_s


def multiSims(sim, rcp):
	'''create a requested simulations for 1 RCP and documented each in a csv file for random csp variables'''

	#guardians
	assert isinstance(sim, int), 'number of simulation must be an integer'
	assert rcp == 2.6 or rcp == 4.5 or rcp == 6.0 or rcp == 8.5, 'Must choose a valid RCP!'

	#loops to create requested simulations
	for i in range(sim):
		csp = uniform(1.0,7.0)
		run_simmod(1900, 2100, rcp, csp, 'results/rcp'+str(rcp)+'-0'+str(i+1)+'.csv')


def spaghettiplot(sim, years, rcp, color):
	'''create a spaghetti plot for each RCPs'''

	#guardians
	assert isinstance(sim, int), 'number of simulation must be an integer'
	assert rcp == 2.6 or rcp == 4.5 or rcp == 6.0 or rcp == 8.5, 'Must choose a valid RCP!'

	#generate files
	#multiSims(sim, rcp)

	#loops to create a spaghetti plot
	for i in range(sim):
		x = []
		x = numpy.loadtxt('results/rcp'+str(rcp)+'-0'+str(i+1)+'.csv', usecols =(30), delimiter =',', skiprows = 1, unpack = True)
		if i == 0:
			plot(yrs, x, color, label = 'RCP'+str(rcp))
		else:
			plot(yrs, x, color)

			
#int var
yrs = getYears()


#call functions
spaghettiplot(10, yrs, 2.6, 'b-')
spaghettiplot(10, yrs, 4.5, 'g-')
spaghettiplot(10, yrs, 6.0, 'y-')
spaghettiplot(10, yrs, 8.5, 'r-')

#making the graph
legend(loc = 'upper left')                                             # Add a legend to the graph.
title("Projected Change in Temperature over the year for each RCP")    # Set the title for the plot
xlabel("Year")                                                         # Label the x axis.
ylabel("Degree Celcius")                                               # Label the y axis.
grid(True)                                                             # Turn on the grid lines.
show()                                                                 # Make the graph show.


