#Maggie and Long

#import packages
from random import *
from funx import *
from graphics import *

#int var
sqSize = 70
winSize = sqSize*5
win = GraphWin('Tic-Tac-Toe game', winSize, winSize)
win.setBackground('white')
win.setCoords(0,0, winSize, winSize)

#call func
gameBoard(win)
