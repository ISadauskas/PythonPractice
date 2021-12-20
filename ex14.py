# # Exercise 14
#
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
#  Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#  Go back and do Exercise 5 using sets, and write the solution for that in a different function.


# Main:
def remove_main(list):
    return set(list)

# Extra 1:
def remove_extra1(list):
    result = []
    for elem in list:
        if elem not in result:
            result.append(elem)
    return result

import random

c = []

for elem in range(0, 20):
    c.append(random.randint(1, 10))

print("Before removal: " + str(c))
print("After removal: " + str(remove_extra1(c)))


