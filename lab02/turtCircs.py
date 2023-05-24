#Christine and Long

# Import modules
from random import *
from turtle import *
from math import *

print(screensize())
# Turtle window is 400 x 300.

# initialize variables (give variables their 1st values - init var)
sue = Turtle()
totalArea = 0

# Ask user for number of circles
numCircle = int(input("How many circle you want to draw?"))

#loop to draw circles
for counter in range(1, numCircle+1):
	#move turtle to random location
	sue.penup()
	x = randint(-150,150)
	y = randint(-150,150)
	sue.goto(x, y)
	sue.pendown()

	#draw circle with random radius
	r = randint(10,50)
	sue.circle(r)

	#calculate the area and the total area, print the area
	area = round((pi*(r**2)),2)
	totalArea = round((totalArea+area),2)
	print("The area of the circle", counter, "is", area, ".")
	
	#on the next to last loop
	if counter == numCircle - 1:
		print("Special Alert!")
	
	#state diagram
		print()
		print("State Diagram:")
		print("counter -->", counter)
		print("r -->", r)
		print("Sue in turtle:")
		print("x -->", x)
		print("y-->", y)
		print("area -->", area)
		print("totalArea -->", totalArea)
		print("counter -->", numCircle)
		print()

#print the total area
print()
print("The total area is:", totalArea)	
	
# blackscreen remains
exitonclick()