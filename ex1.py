# # Exercise 1

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# Main + extra1 + extra2:
age = int(input("Please enter your age: "))
times = int(input("How many times would you like to repeat your message: "))

print(("You will turn 100 years old in " + str(100 - age + 2022) + "\n") * times)

