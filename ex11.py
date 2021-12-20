# # Exercise 11
#
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.)

def get_divisors(number):
    a = [elem for elem in range(1, number + 1) if number % elem == 0]
    return len(a)

num = int(input("Please input a number to check for: "))
if get_divisors(num) == 2:
    print("The number is prime")