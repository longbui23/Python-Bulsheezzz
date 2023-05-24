#Maggie and Long
#Tic-Tac-Toe

#Import packages
from funx import *

#int var
posnum = ['1', '2', '3', '4', '5', '6', '7', '8', '9']        #assign number to position
boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']         #assign empty boxes to play
gameOver = False                                              #variable to continue the game in while loop

#call func
print('Now lets play Tic-Tac-Toe!!!!!')
print()
prBoard(posnum)
print()

#while loop for Game Over:

#one turn
while gameOver == False and boardoverload(boxes) == False:
	#player turn
	usermove(boxes)                                               #usermove
	print()
	prBoard(boxes)                                                #change the board of the usermove to x and print the board
	print()

	#game-check
	if checkWin(boxes) == True:                                   #check if the Player has won or not
		print('Congrats! You have won the game!')
	elif boardoverload(boxes) == True:
		print('The computer could not make any valid move!')      #inform player that the computer cannot make any valid move
	else:
		#computer turn
		print('It is now the computer turn:')
		compmove(boxes)                                           #computer move     
		print()
		prBoard(boxes)                                            #change the board of the compmove to o and print the board
		print()
		if checkWin(boxes) == True:                               #check if the computer has won or not
			print('You have lost the game to a mere computer!!')
			gameOver = True
