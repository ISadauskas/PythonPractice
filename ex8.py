# # Exercise 8
#
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

game = "Yes"

while game == "Yes":
    player1 = str(input("Player 1 choose: "))
    while (player1 != "Scissors") or (player1 != "Paper") or (player1 != "Rock"):
        player1 = str(input("Player 1 choose:"))
    player2 = input("Player 2 choose:")
    while player2 != "Scissors" or player2 != "Paper" or player2 != "Rock":
        player2 = input("Player 2 choose:")
    
    if player1 == "Scissors" and player2 == "Paper":
        print("Player 1 wins")
    elif player1 == "Paper" and player2 == "Rock":
        print("Player 1 wins")
    elif player1 == "Rock" and player2 == "Scissors":
        print("Player 1 wins")
    elif player2 == player1:
        print("Draw")
    else:
        print("Player 2 wins")

    game = input("Another game?")
