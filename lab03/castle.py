from graphics import*
from random import*

window = GraphWin("background", 420, 300)
window.setCoords(0, 0, 420, 300)
window.setBackground("white")

#int var
y = 10

#drawing bricks vertically
for level in range(1,21):
	x = 0
	y = y + 10	
	if y % 20 == 10:
			x = x + 14
			brick = Rectangle(Point(x,y),Point(x+14,y+10))
			brick.setFill(color_rgb( randint(100, 140), randint(100, 140), randint(100, 140)))
			brick.draw(window)
			x = x - 7
		
# drawing grey bricks horizontally
	for length in range(1,28):
		x = x + 14
		if x == 385:
			brick = Rectangle(Point(x,y),Point(x+7,y+10))
			brick.setFill(color_rgb( randint(100, 140), randint(100, 140), randint(100, 140)))
			brick.draw(window)
		else:
			brick = Rectangle(Point(x,y),Point(x+14,y+10))
			brick.setFill(color_rgb( randint(100, 140), randint(100, 140), randint(100, 140)))
			brick.draw(window)

#buiding bombardments
#int var
x = 7
y = y + 10
for numBombard in range (1,5):
	bombardment = Rectangle(Point(x,y),Point(x + 56,y + 30))
	bombardment.setFill("grey")
	bombardment.setOutline("Grey")
	bombardment.draw(window)
	for numDefsn in range (1,5):
		y = 250
		defsn = Rectangle(Point(x,y),Point(x + 8,y + 10))
		defsn.setFill("grey")
		defsn.setOutline("Grey")
		defsn.draw(window)
		x = x + 16
	x = x + 49
	y = y - 30

#buidling tower
x = 56
y = 20
for number in range(1,4):
	tower = Rectangle(Point(x,y),Point(x+70,y+200))
	tower.draw(window)
	x = x + 112

#buiding upper gate
rHead = Circle(Point(203, 100), 21)
rHead.setFill("red")
rHead.draw(window)

#building lower gate
rGate = Rectangle(Point(182,30),Point(224,100))
rGate.setFill("red")
rGate.setOutline("red")
rGate.draw(window)
		
#ending stuff
window.getMouse()
window.close()