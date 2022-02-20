# # Exercise 10

# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. 
# (Hint: Remember list comprehensions from Exercise 7).

# Extra:

# Randomly generate two lists to test this

# Main
import random

a = random.sample(range(0, 31), random.randint(1, 15))
b = random.sample(range(0, 31), random.randint(1, 15))
print("List a:", a, "\nList b:", b, "\nOverlap:", [elementA for elementA in set(a) for elementB in set(b) if elementA == elementB])

