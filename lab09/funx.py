#Maggie and Long

#import packages
from time import *
from random import *
from graphics import *


#create function
def prRow(box1, box2, box3):
	'''print a particular row of 3 boxes'''
	print(' ' + box1 + ' | ' + box2 + ' | ' + box3)


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

	if checklist[0] == checklist[1] == checklist[2] != ' ' or checklist[
	  3] == checklist[4] == checklist[5] != ' ' or checklist[6] == checklist[
	   7] == checklist[8] != ' ' or checklist[0] == checklist[4] == checklist[
	    8] != ' ' or checklist[2] == checklist[4] == checklist[
	     6] != ' ' or checklist[0] == checklist[3] == checklist[
	      6] != ' ' or checklist[1] == checklist[4] == checklist[
	       7] != ' ' or checklist[2] == checklist[5] == checklist[8] != ' ':
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
		if (uMove in valids) and (move[int(uMove) - 1] == ' '):
			move[int(uMove) - 1] = 'x'
			uValid = True


def compmove(move):
	'''generate a random move for computer's turn'''
	uValid = False
	while uValid == False:
		compMove = randint(1, 9)
		if move[compMove - 1] == ' ':
			move[compMove - 1] = '0'
			uValid = True


#PROG09 STARTS HERE
def gameBoard(bxSize, win):
	'''draw the entire board'''

	#int var
	#Curtain
	#int var
	curtain = Rectangle(Point(0,0),
						Point(bxSize*5, bxSize*5)
	)
	#coloring
	curtain.setFill('light blue')
	curtain.draw(win)
	
	#Loop to draw square vertically
	for j in range(3):
		#loop to draw square horizontally
		for i in range(3):
			box = Rectangle(Point(i * bxSize, j * bxSize),
			                Point((i + 1) * bxSize, (j + 1) * bxSize))
			box.setFill('white')

			#output
			box.draw(win)

			
	#user: X and comp: 0
	#int var
	user = Text(Point(bxSize, bxSize * 4), 'User: X')
	comp = Text(Point(bxSize, bxSize * 4.5), 'Computer: O')

	#coloring text
	user.setFill('green')
	comp.setFill('red')

	#output
	user.draw(win)
	comp.draw(win)


def drawX(x, y, sqSize, win):
	'''draw X on screen'''

	#int var
	rec1 = Polygon(Point(x + sqSize * 0.1, y + sqSize * 0.1),
	               Point(x + sqSize * 0.2, y + sqSize * 0.1),
	               Point(x + sqSize * 0.9, y + sqSize * 0.8),
	               Point(x + sqSize * 0.8, y + sqSize * 0.8))

	rec2 = Polygon(Point(x + sqSize * 0.8, y + sqSize * 0.1),
	               Point(x + sqSize * 0.9, y + sqSize * 0.1),
	               Point(x + sqSize * 0.2, y + sqSize * 0.8),
	               Point(x + sqSize * 0.1, y + sqSize * 0.8))

	#coloring
	rec1.setFill('green')  #coloring
	rec1.setOutline('green')
	rec2.setFill('green')   #coloring
	rec2.setOutline('green')

	#output
	rec1.draw(win)
	rec2.draw(win)


def drawO(x, y, sqSize, win):
	'''draw O on screen'''

	#int var
	out_cir = Circle(Point(x + sqSize * 0.5, y + sqSize * 0.5), sqSize * 0.4)
	in_cir = Circle(Point(x + sqSize * 0.5, y + sqSize * 0.5), sqSize * 0.3)

	#coloring
	out_cir.setFill('red')
	out_cir.setOutline('red')
	in_cir.setFill('white')
	in_cir.setFill('white')

	#output
	out_cir.draw(win)
	in_cir.draw(win)


def userGUIMove(sqSize, board, win):
	'''identify user's move and draw it on screen'''

	#inform user
	inform_text = Text(Point(sqSize, sqSize * 3.5), "User's turn:")
	inform_text.setFill('green')
	inform_text.draw(win)

	#int var
	valids = ['1','2','3','4','5','6','7','8','9']
	move = '0'
	uValid = False

	#while loop
	while uValid == False:
		#GetUserclick
		usMove = win.getMouse()
		xPos = usMove.getX()
		yPos = usMove.getY()

		#Categorize user's move and initiate x and y coordinate for each categories
		#top boxes
		if sqSize * 2 <= yPos <= sqSize * 3:
			y = sqSize * 2
			if 0 <= xPos <= sqSize * 1:
				move = '1'
				x = 0
			elif sqSize * 1 <= xPos <= sqSize * 2:
				move = '2'
				x = sqSize
			elif sqSize * 2 <= xPos <= sqSize * 3:
				move = '3'
				x = sqSize * 2
			else:
				print('Invalid move!')
		#middle boxes
		elif sqSize * 1 <= yPos <= sqSize * 2:
			y = sqSize * 1
			if 0 <= xPos <= sqSize * 1:
				move = '4'
				x = 0
			elif sqSize * 1 <= xPos <= sqSize * 2:
				move = '5'
				x = sqSize
			elif sqSize * 2 <= xPos <= sqSize * 3:
				move = '6'
				x = sqSize * 2
			else:
				print('Invalid move!')
		#bottom line
		elif 0 <= yPos <= sqSize * 1:
			y = 0
			if 0 <= xPos <= sqSize * 1:
				move = '7'
				x = 0
			elif sqSize * 1 <= xPos <= sqSize * 2:
				move = '8'
				x = sqSize * 1
			elif sqSize * 2 <= xPos <= sqSize * 3:
				move = '9'
				x = sqSize * 2
			else:
				print('Invalid move!')

	#output
		if (move in valids) and board[int(move) - 1] == ' ':
			board[int(move) - 1] = 'x'
			drawX(x, y, sqSize, win)
			inform_text.undraw()
			uValid = True
	return board


def compGUImove(sqSize, board, win):
	'''assign random move for computer and sho it on screen'''

	#inform text
	inform_textC = Text(Point(sqSize,sqSize*3.5),"Computer's turn:")
	inform_textC.setFill('red')
	inform_textC.draw(win)
	
	#int var
	valids = ['1','2','3','4','5','6','7','8','9']
	move = '0'
	uValid = False

	#while loop
	while uValid == False:
		#AssignCoords
		xPos = randint(0, sqSize * 3)
		yPos = randint(0, sqSize * 3)

		#Categorize user's move
		#top line
		if sqSize * 2 <= yPos <= sqSize * 3:
			y = sqSize * 2
			if 0 <= xPos <= sqSize * 1:
				move = '1'
				x = 0
			elif sqSize * 1 <= xPos <= sqSize * 2:
				move = '2'
				x = sqSize
			elif sqSize * 2 <= xPos <= sqSize * 3:
				move = '3'
				x = sqSize * 2
			else:
				print('Invalid move!')
		#middle line
		elif sqSize * 1 <= yPos <= sqSize * 2:
			y = sqSize
			if 0 <= xPos <= sqSize * 1:
				move = '4'
				x = 0
			elif sqSize * 1 <= xPos <= sqSize * 2:
				move = '5'
				x = sqSize
			elif sqSize * 2 <= xPos <= sqSize * 3:
				move = '6'
				x = sqSize * 2
			else:
				print('Invalid move!')
		#bottom line
		elif 0 <= yPos <= sqSize * 1:
			y = 0
			if 0 <= xPos <= sqSize * 1:
				move = '7'
				x = 0
			elif sqSize * 1 <= xPos <= sqSize * 2:
				move = '8'
				x = sqSize
			elif sqSize * 2 <= xPos <= sqSize * 3:
				move = '9'
				x = sqSize * 2
			else:
				print('Invalid move!')

	#output
		if move in valids and board[int(move) - 1] == ' ':
			board[int(move) - 1] = 'O'
			drawO(x, y, sqSize, win)
			inform_textC.undraw()
			uValid = True
	return board


def drawText(x , y, txt, col, win):
	'''draw text on screen surrounding by a box'''
	
	#text
	endText = Text(Point(x, y), txt)
	endText.setTextColor(col)
	endText.draw(win)


def drawBox(x1, y1, x2, y2, col, win):
	'''draw a box'''
	box = Rectangle(Point(x1, y1), Point(x2, y2))
	box.setFill(col)
	box.draw(win)


def playMatch(sqSize, win):
	'''play a match of Tic-Tac-Toe'''
	#draw boargame
	gameBoard(sqSize, win)

	#int var
	boxes = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	endGame = False

	#loop for multiple turns
	while endGame == False:
		#check for tie
		if boardoverload(boxes) == True:
			drawBox(sqSize, sqSize*1.5, sqSize*3.5, sqSize*2.5, color_rgb(204, 255, 225), win)
			drawText(sqSize*2.2, sqSize*2, 'This is a tie', 'yellow', win) 
			endGame = True
		else:
			#user's move
			userGUIMove(sqSize, boxes, win)
			if checkWin(boxes) == True:
				drawBox(sqSize, sqSize*1.5, sqSize*3.5, sqSize*2.5, color_rgb(204, 255, 255), win)
				drawText(sqSize*2.2, sqSize*2, 'You have won the game!', 'green', win)
				endGame = True
			else:
				sleep(1)
				#computer move
				compGUImove(sqSize, boxes, win)
				if checkWin(boxes) == True:
					drawBox(sqSize, sqSize*1.5, sqSize*3.5, sqSize*2.5, color_rgb(205, 255, 255), win)
					drawText(sqSize*2.2, sqSize*2, 'You have lost the game!', 'red', win)
					endGame = True


def playAgain(sqSize, win):
	'''ask player if they want to play again'''

	#int var
	playAgain = True

	#while loop to recieve player's response
	while playAgain == True:
		
		#int var
		#draw question box
		bigBox = drawBox(sqSize, sqSize, sqSize*3, sqSize*3, color_rgb(205, 255, 255), win)
		bigText = drawText(sqSize*2, sqSize*2, "Play again?", "black", win)
	
		#draw yes box
		yesBox = drawBox(sqSize*1.1, sqSize*1.1, sqSize*1.5, sqSize*1.5, 'white', win)
		yesText = drawText(sqSize*1.3, sqSize*1.3, "yes", "green", win)
	
		#draw no box
		noBox = drawBox(sqSize*2.5, sqSize*1.1, sqSize*2.9, sqSize*1.5, 'white', win)
		noText = drawText(sqSize*2.7, sqSize*1.3, "no", 'red', win)

		#getUserclick
		usMove = win.getMouse()
		xPos = usMove.getX()
		yPos = usMove.getY()

		#conditional to direct user whether he/she wants to play again
		if sqSize*1.1 <= xPos <= sqSize*1.5 and sqSize*1.1 <= yPos <= sqSize*1.5:            #if player's click yes
			playMatch(sqSize, win)
		elif sqSize*2.5 <= xPos <= sqSize*2.9 and sqSize*1.1 <= yPos <= sqSize*1.5:          #if player's click no
			drawBox(sqSize, sqSize, sqSize*3, sqSize*3, color_rgb(205, 255, 255), win)
			drawText(sqSize*2, sqSize*2, 'Thank you for playing!', 'red', win)
			playAgain = False


def fullGame(sqSize, win):
	'''play a full game'''
	#playgame
	playMatch(sqSize, win)
	sleep(1)
	playAgain(sqSize, win)
	sleep(1)
	
	#Ending
	win.close()