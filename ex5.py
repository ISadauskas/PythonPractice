# # Exercise 5
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

# Main program:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for element in a :
    if element in b:
        if element not in c:
            c.append(element)

print(c)

# Extra 1:
a = []
b = []
c = []

n = random.randint(0, 20)

for x in range(n):
    rand = random.randint(0, 15)
    a.append(rand)

n = random.randint(0, 20)

for x in range(n):
    rand = random.randint(0, 15)
    b.append(rand)

a.sort()
b.sort()

print("List a: " + str(a))
print("List b: " + str(b))

for element in a :
    if element in b:
        if element not in c:
            c.append(element)

print("Shared numbers between a and b: " + str(c))

# Extra 2:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
c = [element for element in a if element in b if element not in c]

print(c)
