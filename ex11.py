# # Exercise 11

# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

def checkPrime(integer):
    a = range(1, integer + 1)
    if(len([element for element in a if integer % element == 0]) == 2):
        return True
    else:
        return False

number = int(input("Please input a number to check: "))
if(checkPrime(number) == True):
    print("The number", number, "is a prime")
else:
    print("The number", number, "is not a prime")