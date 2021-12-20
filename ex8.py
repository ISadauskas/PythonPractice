# # Exercise 8
#
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

game = "Y"

while game == "Y":
    player1 = input("Player 1 lease choose your sign: ")
    while (player1 != "S" and player1 != "R" and player1 != "P"):
        player1 = input("Please choose your sign: ")

    player2 = input("Player 2 please choose your sign: ")
    while (player2 != "S" and player2 != "R" and player2 != "P"):
        player2 = input("Please choose your sign: ")

    if player1 == "S" and player2 == "P":
        print("Player 1 wins")
    elif player1 == "P" and player2 == "R":
        print("Player 1 wins")
    elif player1 == "R" and player2 == "S":
        print("Player 1 wins ")
    elif player1 == player2:
        print("Draw")
    else:
        print("Player 2 wins")

    game = input("Another game?: ")


