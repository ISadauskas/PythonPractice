# # Exercise 9
#
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

target = random.randint(1, 9)

game = ""
actual = -1
count = 0

while(actual != target):
    actual = input("Please take a guess: ")

    if(str(actual) == "Exit"):
        print("Exiting...")
        break
    
    actual = int(actual)

    if(actual > target):
        print("Too high")
        count += 1
    elif (actual < target):
        print("Too low")
        count += 1
    else:
        print("You got it, good job! The number was: " + str(target))
        count += 1
        print("Your number of guesses was: " + str(count))