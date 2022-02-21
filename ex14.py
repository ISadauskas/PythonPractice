# # Exercise 14

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random


def noDupesMain(list):
    dupeless = []
    for element in list:
        if element not in dupeless:
            dupeless.append(element)
    return dupeless

def noDupesExtra(list):
    dupeless = set(list)
    return dupeless

a = []

for i in range(0,15):
    a.append(random.randint(1,10))

print("Your list before removing duplicates: ", a)
print("Your list after rmoving duplicates with a loop: ", noDupesMain(a))
print("Your list after removing duplicates using sets: ", noDupesExtra(a))
