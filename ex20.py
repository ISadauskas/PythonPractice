# # Exercise 20

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

import random

def findMiddle(arr):
    if len(arr) % 2 == 0:
        return int(len(arr) / 2)
    else:
        return int(len(arr) / 2 - 0.5)


def findMain(arr, target):
    if target in arr:
        return True
    else:
        return False

def binarySearch(arr, target):
    while len(arr) != 1:
        if arr[findMiddle(arr)] == target:
            return True
        elif arr[findMiddle(arr)] > target:
            arr = arr[:findMiddle(arr)]
        else:
            arr = arr[findMiddle(arr):]

    if arr[0] == target:
        return True
    else:
        return False


if __name__ == "__main__":
    a = sorted(random.sample(range(0, 21), random.randint(1, 20)))
    num = random.randint(0, 20)
    print("Is ", num, "in array", a, "?\n", binarySearch(a, num))
    

