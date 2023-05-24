#Maggie and Long

#import packages
from time import *
from random import*
from graphics import*

#create function

def prRow (box1, box2, box3):
	'''print a particular row of 3 boxes'''
	print(' ' + box1 + ' | ' + box2+' | ' + box3)


def prBoard(movelist):
	'''print the entire board'''
	divider = '---+---+---'
	prRow(movelist[0], movelist[1], movelist[2])
	print(divider)
	prRow(movelist[3], movelist[4], movelist[5])
	print(divider)
	prRow(movelist[6], movelist[7], movelist[8])


def checkWin(checklist):
	'''check to see if there is a winner, return True if there is and False otherwise'''
	winner = False
	
	if checklist[0] == checklist[1] == checklist[2] != ' ' or checklist[3] == checklist[4] == checklist[5] != ' ' or checklist[6] == checklist[7] == checklist[8] != ' ' or checklist[0] == checklist[4] == checklist[8] != ' ' or checklist[2] == checklist[4] == checklist[6] != ' ' or checklist[0] == checklist[3] == checklist[6] != ' ' or checklist[1] == checklist[4] == checklist[7] != ' ' or checklist[2] == checklist[5] == checklist[8] != ' ':
		winner = True
	
	return winner


def boardoverload(board):
	'''check whether it is a tie or not'''
	for item in board:
		if item == ' ':
			return False
	else:
		print('It is a tie!')
		return True


def usermove(move):
	'''Let a user enter a move and check whether the move is ok or not'''
	valids = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	uValid = False
	while uValid == False:
		uMove = input('Which position you want to tic-tac-toe ? >>')
		if (uMove in valids) and (move[int(uMove)-1] == ' '):
			move[int(uMove)-1] = 'x'
			uValid = True


def compmove(move):
	'''generate a random move for computer's turn'''
	valids = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	uValid = False
	while uValid == False:
		uMove = str(randint(1,9))
		if (uMove in valids) and (move[int(uMove)-1] == ' '):
			move[int(uMove)-1] = '0'
			uValid = True


#PROJECT09 STARTS FROM HERE
def gameBoard(win):
	'''draw the entire board'''
	
	#int var
	bxSize = 50

	#Loop to draw square vertically
	for j in range (3):
		#loop to draw square horizontally
		for i in range (3):
			box = Rectangle(Point(i*bxSize, j*bxSize),Point((i+1)*bxSize, (j+1)*bxSize))
			box.draw(win)

	#user: X and comp: 0
	user = Text(Point(bxSize,bxSize*6),'User: X')
	comp = Text(Point(bxSize,bxSize*5),'Computer: O')
	user.draw(win)
	comp.draw(win)
	