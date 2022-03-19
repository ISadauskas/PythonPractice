# # Exercise 32

# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
# In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# Optional additions:

# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!

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

def drawHangman(count):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''']

    if count == 1:
        print(HANGMANPICS[5])
    elif count == 2: 
        print(HANGMANPICS[4])
    elif count == 3:
        print(HANGMANPICS[3])
    elif count == 4:
        print(HANGMANPICS[2])
    elif count == 5:
        print(HANGMANPICS[1])
    else:
        print(HANGMANPICS[0])

while True:
    count = 0
    target = pickWord()
    guess = ['_' for i in range(len(target))]
    usedLetters = []

    while "".join(guess) != target:
        if count == 6:
            print("You have lost")
            break

        letter = str(input("Please pick a letter: ")).capitalize()
        if letter not in usedLetters:
            count += 1
            usedLetters.append(letter)
            for i in range(len(target)):
                if target[i] == letter:
                    guess[i] = letter
        else:
            continue
        print("".join(guess))
        drawHangman(count)
        print("You have %i guesses left" %(6 - count))


    game = str(input("Another game? [y/n]"))
    if game == 'n':
        break
