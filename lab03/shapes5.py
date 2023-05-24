#Ray and Long
from graphics import*

#create window
window = GraphWin("shapes5", 600, 600)
window.setCoords(0, 0, 600, 600)

#blue triangle
bTri = Polygon(Point(10, 10), Point(70, 70), Point(100,10))
bTri.setFill("blue")
bTri.draw(window)

#redsquare
rSqr = Rectangle(Point(590, 590),Point(540, 540))
rSqr.setFill("red")
rSqr.draw(window)

#greenCircle
gCir = Circle(Point(550,50),30)
gCir.setFill("green")
gCir.draw(window)

#yellow hexagon
yHex = Polygon(Point(50,590),Point(10, 565), Point(30, 530), Point(70, 530), Point(90, 565))
yHex.setFill("yellow")
yHex.draw(window)

#light blue diamond
lbDmd = Polygon(Point(220,300), Point(300,400), Point(380,300), Point(300,200))
lbDmd.setFill(color_rgb(152, 245, 255))
lbDmd.draw(window)

#ending stuff
window.getMouse()
window.close()