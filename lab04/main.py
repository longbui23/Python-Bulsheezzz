#snowThem.py, a graphics program 
#Talia and Long

from graphics import * 
from random import *

#st02-window appears
window = GraphWin("the snowThems approach", 500,500)
window.setCoords(0, 0, 500, 500)

#st03-BGset

def drawGB(width, height, color, window):
	'''draw Back Ground'''
	background = Rectangle(Point(0, 0), Point(width, height))
	background.setFill(color)
	background.draw(window)

backW = 500
backH = 500
backC = "light blue"

drawGB(backW, backH, backC, window)


#st04-draw circle
def drawCircle(cX, cY, cRad, cColor, window):
	'''draw Circle'''
	circle = Circle(Point(cX, cY), cRad)
	circle.setOutline(cColor)
	circle.setFill(cColor)
	circle.draw(window)

#int var
x = 20
y = 480
rad = 10

#drawCircle(x, y, rad, "white", window)
#drawCircle(x, y-2*rad, rad*1.2, "white", window)

#st05-draw body
def drawBody(bX, bY, bRad, bColor, window):
	'''draw Body of the snowman'''
	for counter in range(3):
		drawCircle(bX, bY, bRad, bColor, window)
		bY = bY - bRad
		bRad =  bRad*1.2
		bY = bY - bRad + bRad*0.5

#drawBody(x, y, rad, "white", window)


# #st06-draweye
def drawEye(eX, eY, eRad, eColor, window):
	'''draw 1 eye of the snowman'''
	drawCircle(eX - eRad/4.0, eY + eRad/4.0, eRad/10.0, eColor, window)

#drawEye(x, y, rad, "black", window)

#st07 - draws 2 eyes
def drawEyes(esX, esY, esRad, esColor, window):
	'''draw 2 eyes of the snowman'''
	for i in range (2):
		drawCircle(esX-esRad/4.0, esY+esRad/4.0, esRad/10.0, esColor, window)
		esX = esX + esRad/2.0
	
#drawEyes(x, y, rad, "black", window)

#st08 - draws nose
		'''draw nose of the snowmen'''
def drawNose(nX, nY, nColor, window):
	
	nose = Polygon(Point(nX-rad/4.0, nY),Point(nX+rad/4.0,nY), Point(nX, nY-rad/2.0))
	nose.setFill(nColor)
	nose.draw(window)

#drawNose(x, y, "orange", window)

#st09-draw face
	'''draw face of the snowman'''
def drawFace(fX, fY, fRad, window):
	drawEyes(fX, fY, fRad, "black", window)
	drawNose(fX, fY, "orange", window)

	
#drawFace(x,y,color,window)

#st10-draw1 snowthem
	'''draw 1 snowthem'''
def drawSnowthem(tX, tY, tRad, tcolor, window):
	drawBody(tX, tY, tRad, tcolor, window)
	drawFace(tX, tY, tRad, window)

#color = "white"

#drawSnowthem(x, y, rad, color, window)

#draw hill
hill = Polygon(Point(0,0),Point(0,500),Point(500,0))
hill.setFill("white")
hill.draw(window)

#st11-draw many snowthem
for i in range(50):
	if i % 3== 0:
		color = color_rgb(0,255,255)
	elif i % 3 == 1:
		color = color_rgb(255,192,203)
	else:
		color = "light green"
	x = x + randint(-1,5)*i
	y = y - randint(1,3)*i
	rad = rad + i/6
	drawSnowthem(x, y, rad, color, window)

window.getMouse()
window.close()

