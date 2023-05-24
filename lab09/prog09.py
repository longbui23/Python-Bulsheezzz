#Maggie and Long

#import packages
from funx import*


#int var
sqSize = 100
winSize = sqSize*5
win = GraphWin('Tic-Tac-Toe game', winSize, winSize)


#output
win.setBackground('light blue')
win.setCoords(0,0, winSize, winSize)


#intro
startText = Text(Point(sqSize*2.5, sqSize*2.5),"Tic-Tac-Toe!! Noughts and crosses!!")
startText.setFill('blue')
startText.setStyle('italic')
startText.draw(win)
sleep(3)
startText.undraw()


#full game
fullGame(sqSize, win)