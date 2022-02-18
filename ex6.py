# # Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Please imput a string: "))

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

