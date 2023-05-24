# assess

# program name and programmers' names

# imports
import autonomous_vehicles as av
from matplotlib.pyplot import * 
from random import*

#selfish car
def selfishCar(sce):
	'''selfish car would always save passenger'''
	#might change later to include other senarios where it is kinder and kills less people if there are passengers in both lanes and no barriers
	if sce.left_barrier_exists() == True:
		return "Swerve"
	else:
		return 'Stay'

#numDead
def numDead(lane, sce):
	'''return the number of fatalities that occured in a specified lane'''
	numDed = 0
	if lane == 'left' or lane == 'Stay': 
		if sce.left_barrier_exists() == True:
			numDed = sce.num_passengers()
		else:
			numDed = sce.left_num_pedestrians()
	elif lane == 'right' or lane == 'Swerve':
		if sce.right_barrier_exists() == True:
			numDed = sce.num_passengers()
		else: 
			numDed = sce.right_num_pedestrians()
	return(numDed)

#Utilitarian car
def utilCar(sce):
	'''building cars based on utilitarianist rules'''
	if numDead('right', sce) >= numDead('left', sce):
		return 'Stay'
	else:
		return 'Swerve'

# A Kantian Car
def kantcar(sce):
	"""car that follows Kantain rules"""
	if (sce.left_barrier_exists() == True or sce.left_num_pedestrians() >= 1) and sce.right_num_pedestrians() == 0:
		return 'Swerve'
	else:
		return 'Stay'
		
		
# constructor method creates a Scenario object
# s = av.Scenario(2, True, 5, True, False, 5, True)
#s.randomize()

#Testing area
# assert selfishCar(s) == "Swerve", "Stayed but should have swerve."
# numDead('left', s)
# assert utilCar(s) == 'Stay', 'Should have stayed!' 
# assert kantcar(s) == 'Stay', 'Should have stayed!'


# sen1 = av.Scenario(3, False, 4, True, False, 9, True)
# assert selfishCar(sen1) == "Stay", "Swerved but should have stayed."
# numDead('right', sen1)
# assert utilCar(sen1) == 'Stay', 'Should have stayed!' 
# assert kantcar(sen1) == 'Stay', 'Should have stay'


# sen2 = av.Scenario(4, True, 2, True, False, 0, True)
# assert selfishCar(sen2) == "Swerve", "Swerved but should have stayed."
# numDead('left', sen2)
# assert utilCar(sen2) == 'Swerve', 'Should have swerve!' 
# assert kantcar(sen2) == 'Swerve', 'Should have swerve!'


# sen3 = av.Scenario(6, False, 6, True, False, 7, True)
# assert selfishCar(sen3) == "Stay", "Swerved but should have stayed."
# numDead('right', sen3)
# assert utilCar(sen3) == 'Stay', 'Should have stayed!'
# assert kantcar(sen3) == 'Stay', 'Should have stayed!'

#C1
# def selfCarTest (trials):
# 	'''test for selfish car'''

# 	#int var
# 	sum = 0
# 	s = av.Scenario()

# 	#loop
# 	for i in range(trials):
# 		s.randomize()
# 		sum = sum + numDead(selfishCar(s),s)

# 	#print 
# 	print('The average number of death for selfish car is:', sum/trials)
			
# # selfCarTest(10000)

# #C2
def utilCarTest (trials):
	#int var
	s = av.Scenario()
	sum = 0

# 	#loop
	for i in range(trials):
		s.randomize()
		sum= sum +numDead(utilCar(s),s)
		
	print('The average number of death for utilitarian car is:', sum/trials)

# utilCarTest(100000)

#C3
x = []
y = []

s = av.Scenario()
pct_selfish = 1

for fract in range(100):
	total_dead = 0
	for i in range(1000):                                           
		s.randomize()
		if randint(1,100) < pct_selfish:
			if(selfishCar(s) == 'Stay'):
				total_dead = total_dead + numDead('left',s)
			else:
				total_dead = total_dead + numDead('right',s)
		else:
			if(utilCar(s) == 'Stay'):
				total_dead = total_dead + numDead('left', s)
			else:
				total_dead = total_dead + numDead('right', s)
	x.append(fract/100)
	y.append(total_dead/1000)

	pct_selfish = pct_selfish + 1 

#Generate a plot
scatter (x, y,)
title('Fatalities due to selfish cars')
xlabel('Fractions of selfish car')
ylabel('Death/Scenario')
grid(True)
show()