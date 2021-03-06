# # Exercise 27

# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

# game = [[0, 0, 0],
# 	      [0, 0, 0],
# 	      [0, 0, 0]]
# The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

# game = [[0, 0, X],
# 	      [0, 0, 0],
# 	      [0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.

# Things to note:

# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
# Bonus:

# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.

board = [[0, 0, 0],
	     [0, 0, 0],
         [0, 0, 0]]

def checkForFull(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                count += 1
    if count == 9:
        return True
    else:
        return False

def checkIfOccupied(board, row, column):
    if board[row][column] != 0:
        return True
    else:
        return False 

while True:
    move = input("Please imput the row and column in which to place the X (row,col): ").split(',')
    row = int(move[0]) - 1
    column = int(move[1]) - 1
    if checkIfOccupied(board, row, column): 
        while checkIfOccupied(board, row, column):
            move = input("Please imput the row and column in which to place the X (row,col): ").split(',')
            row = int(move[0]) - 1
            column = int(move[1]) - 1 
    board[row][column] = 'X'

    for i in range(3):
        print(board[i])
    
    if checkForFull(board):
        break

    move = input("Please imput the row and column in which to place the O (row,col): ").split(',')
    row = int(move[0]) - 1
    column = int(move[1]) - 1
    if checkIfOccupied(board, row, column): 
        while checkIfOccupied(board, row, column):
            move = input("Please imput the row and column in which to place the O (row,col): ").split(',')
            row = int(move[0]) - 1
            column = int(move[1]) - 1  
    board[row][column] = 'O'

    for i in range(3):
        print(board[i])
    
    if checkForFull(board):
        break