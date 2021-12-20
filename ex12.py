# # Exercise 12
#
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def ends(list):
    print(list[0])
    print(list[-1])

a = [elem for elem in range(1, 21)]
ends(a)
