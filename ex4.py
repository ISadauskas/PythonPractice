# # Exercise 4

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

target = int(input("Please input a number to check the divisors of : "))

a = range(1, target + 1)

print("List of divisors for the number", target, ":", [element for element in a if target % element == 0])