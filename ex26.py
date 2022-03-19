# # Exercise 26

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. 
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. 
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

def checkIfWon(state):
    for i in range(len(state[0])):

        if state[i][0] == state[i][1] and state[i][0] == state[i][2] and state[i][0] != 0:
            print("Player ", state[i][0], "won")

        if state[0][i] == state[1][i] and state[0][i] == state[2][i] and state[0][i] != 0:
            print("Player ", state[0][i], "won")

    if state[0][0] == state[1][1] and state[0][0] == state[2][2] and state[0][0] != 0:
        print("Player ", state[0][0], "won")
    
    if state[0][2] == state[1][1] and state[0][2] == state[2][0] and state[0][2] != 0:
        print("Player ", state[0][2], "won")


if __name__ == "__main__":
    game = [[1, 2, 0],
	        [2, 1, 0],
	        [2, 1, 1]]

    checkIfWon(game)

    