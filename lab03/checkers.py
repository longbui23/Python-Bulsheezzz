#Ray and Long
from graphics import*

#create window
window = GraphWin("checkerboard", 300, 300)
window.setCoords(0, 0, 300, 300)

#int var
y = 0

#vertical loop
for z in range(8):
	x = 0
	y = y+30

	#horizontal loop
	for t in range(8):
		x = x+30
		rSqr = Rectangle(Point(x, y),Point(x+30, y+30))
		
		#check color
		if int(x+y) % 60 == 0:
			rSqr.setFill("red")
		else:
			rSqr.setFill("black")

		#draw on screen
		rSqr.draw(window)

#ending stuff
window.getMouse()
window.close()