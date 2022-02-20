# # Exercise 8

# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

game = True

while(game == True):
    player1 = str(input("Player 1 - please choose rock, paper or scissors: "))
    while player1 != "rock" and player1 != "paper" and player1 != "scissors":
        player1 = str(input("Player 1 - please choose rock, paper or scissors: "))

    player2 = str(input("Player 2 - please choose rock, paper or scissors: "))
    while player2 != "rock" and player2 != "paper" and player2 != "scissors":
        player2 = str(input("Player 2 - please choose rock, paper or scissors: "))

    if(player1 == player2):
        print("It's a draw!")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    state = str(input("Another game [Y/N]?"))
    if(state == "N"):
        game = False
