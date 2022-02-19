# # Exercise 5
#
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# Main

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for elementA in a:
    for elementB in b:
        if elementA == elementB and elementA not in c:
            c.append(elementA)

print(c)

# Extra 1 + Extra 2
import random
a = random.sample(range(0, 20), random.randint(1, 15))
b = random.sample(range(0, 20), random.randint(1, 15))
c = []
c = [elementA for elementA in a for elementB in b if elementA == elementB and elementA not in c]
print("The common elements between sets", a, "and", b, "are: ", c)
