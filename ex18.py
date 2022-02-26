# # Exercise 18

# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. 
# Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random

if __name__ == "__main__":
    count = 0
    target = str(random.randint(1000, 9999))
    guess = ""
    print(target)
    while target != guess:
        guess = str((input("Please take a guess: ")))
        count += 1
        bull = 0
        cow = 0

        bullArr = []
        
        for i in range(4):
            if target[i] == guess[i]:
                cow += 1
            elif guess[i] in target and guess[i] not in bullArr:
                bull += 1
                bullArr.append(guess[i])
        print("You have", cow, "cows and", bull, "bulls")
    
    print("Congratulations, you number of guesses was: ", count)
    



