# # Exercise 29

# The next step is to put all these three components together to make a two-player Tic Tac Toe game! 
# Your challenge in this exercise is to use the functions from those previous exercises-
# -all together in the same program to make a two-player game that you can play with a friend. 
# There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

# Here are a few things to keep in mind:

# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.


def checkIfWon(board):
    for i in range(len(board[0])):

        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != 0:
            print("Player ", board[i][0], "won")
            return True

        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != 0:
            print("Player ", board[0][i], "won")
            return True

    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != 0:
        print("Player ", board[0][0], "won")
        return True
    
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != 0:
        print("Player ", board[0][2], "won")
        return True

def drawBoard(board):
    print(" ---" * 3)
    for n in range(3):
        print("| %s " % board[0][n], end = '')
        print("| %s " % board[1][n], end = '')
        print("| %s |" % board[2][n], end = '')
        print("\n" + (" ---" * 3))


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
    if board[column][row] != 0:
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
    board[column][row] = 'X'

    drawBoard(board)
    
    if checkIfWon(board):
        o = str(input("Another game [y/n]"))
        if o == 'y':
            board = [[0, 0, 0],
	                [0, 0, 0],
                    [0, 0, 0]]
            continue
        else:
            break


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
    board[column][row] = 'O'

    drawBoard(board)

    if checkIfWon(board):
        o = str(input("Another game [y/n]"))
        if o == 'y':
            board = [[0, 0, 0],
	                [0, 0, 0],
                    [0, 0, 0]]
            continue
        else:
            break
    
    if checkForFull(board):
        break

