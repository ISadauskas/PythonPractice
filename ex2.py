# # Exercise 2

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

# Extras:

# 1) If the number is a multiple of 4, print out a different message.
# 2)  Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#   If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# Main + extra 1

num = int(input("Pick a number: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("The number is divisible by 4")
    else:
        print("The number is divisible by 2, but not by 4")
else:
    print("The number is not divisible by 2")

# Extra 2

num = int(input("Please input a number to check: "))
div = int(input("Please input a number to divide by: "))

if num % div == 0:
    print(num, "evenly divides by", div)
else:
    print(num , "does not evenly divide by", div)