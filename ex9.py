# # Exercise 9

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


# Main + extra 1 + extra 2
import random

target = random.randint(1, 9)
count = 0
guess = 0
while guess != target:
    guess = input("Please input your guess: ")
    if guess == "exit":
        break
    guess = int(guess)
    count += 1
    if guess == target:
        print("Congratulation, you got it!")
    elif guess < target:
        print("Too low")
    else:
        print("Too high")

print("Your number of guesses: ", count)