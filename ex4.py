# # Exercise 4
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Main exercise:
# Short variant
num = int(input("Please enter a number: "))

x = range(1, num + 1)
answer = print([element for element in x if num % element == 0])

# Long variant
for element in x:
    if num % element == 0:
        answer.append(element)

print(answer)