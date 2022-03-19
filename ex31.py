# # Exercise 31

# Let’s continue building Hangman. 
# In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. 
# The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”. 
# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
# For now, let the player guess an infinite number of times until they get the entire word. 
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. 
# Remember to stop the game when all the letters have been guessed correctly! 
# Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

import random

def pickWord():
    lines = []
    with open('sowpods.txt', 'r') as f:
        line = f.readline().strip()
        lines.append(line)
        while line:
            line = f.readline().strip()
            lines.append(line)
    return lines[random.randint(0, len(lines) - 1)]

target = pickWord()
guess = ['_' for i in range(len(target))]
usedLetters = []

while "".join(guess) != target:
    letter = str(input("Please pick a letter: ")).capitalize()
    if letter not in usedLetters:
        usedLetters.append(letter)
        for i in range(len(target)):
            if target[i] == letter:
                guess[i] = letter
    else:
        continue
    print("".join(guess))
    
    