# # Exercise 23

# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

with open("happynumbers.txt") as f:
    happy = [line.rstrip() for line in f]

with open("primenumbers.txt") as f:
    prime = [line.rstrip() for line in f]

print([num for num in prime if num in happy])