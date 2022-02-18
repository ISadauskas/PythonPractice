# # Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
#

# # Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# Main + extra 1:

num = int(input("Please enter a number: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("The number is a multiple of 4")
    else:
        print("The number is even")
else:
    print("The number is odd")

# Extra 2:    

num = int(input("Please enter a number to check by: "))

check = int(input("Please enter a number to divide by: "))

if num % check == 0:
    print("Check divides evenly into num")
else:
    print("Check does not divide evenly into num")
