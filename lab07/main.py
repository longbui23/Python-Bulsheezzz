#import packages
import numpy
from matplotlib.pyplot import *

#create functions
def getYears():
	'''return a list of years from historical_ghgs.csv file'''
	years = numpy.loadtxt("emissions/historical_ghgs.csv", usecols =(0), delimiter =',', skiprows = 1, unpack = True)
	return years


def getC():
	'''return a list documenting amount of carbon emissions from 1765 to 2000'''
	c_emissions_pg = numpy.loadtxt("emissions/historical_ghgs.csv", usecols =(1), delimiter =',', skiprows = 1, unpack = True)
	return c_emissions_pg


def getCH4():
	'''return a list documenting the amount of methane from 1765 to 2000'''
	ch4_emissions_tg = numpy.loadtxt("emissions/historical_ghgs.csv", usecols =(2), delimiter =',', skiprows = 1, unpack = True)
	return ch4_emissions_tg


def getN2O():
	'''return a list documenting the amount of methane from 1765 to 2000'''
	n2o_emissions_tg = numpy.loadtxt("emissions/historical_ghgs.csv", usecols =(3), delimiter =',', skiprows = 1, unpack = True)
	return n2o_emissions_tg


def getYearsa():
	'''return a list of years for the predicted future scenarios'''
	years = numpy.loadtxt("emissions/rcp_2.6_data.csv", usecols =(0), delimiter =',', skiprows = 1, unpack = True)
	return years


def getCO2a(scenario):
	'''return a list documenting the amount of methane of the scenario requested'''

	#guardians
	assert scenario == 2.6 or scenario == 4.5 or scenario == 6.0 or scenario == 8.5, 'Must choose a valid RCP!'

	#documentation
	co2_concentration_ppm = numpy.loadtxt("emissions/rcp_"+str(scenario)+"_data.csv", usecols =(7), delimiter =',', skiprows = 1, unpack = True)
	return co2_concentration_ppm

	
#int var
yrs = getYearsa()
co2_rcp26 = getCO2a(2.6)
co2_rcp45 = getCO2a(4.5)
co2_rcp60 = getCO2a(6.0)
co2_rcp85 = getCO2a(8.5)


#scenario = float(input('Which scenario you want to see?'))	
#plot(getYears(), getCH4(), "r-", label = "Methane")
plot(yrs, co2_rcp26, "b-", label = "RCP2.6")
plot(yrs, co2_rcp45, "r-", label = "RCP4.5")
plot(yrs, co2_rcp60, "g-", label = "RCP6.0")
plot(yrs, co2_rcp85, "y-", label = "RCP8.5")

#making the graph
legend(loc = 'upper left')               # Add a legend to the graph.
title("Projected CO2 concentrations")    # Set the title for the plot
xlabel("Year")                           # Label the x axis.
ylabel("Carbon Concentration (ppm)")     # Label the y axis.
grid(True)                               # Turn on the grid lines.
show()                                   # Make the graph show.

