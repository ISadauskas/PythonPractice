# # Exercise 6

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string  = str(input("Please input a word to check: "))

if string == string[::-1]:
    print("The word " + string + " is a palindrome")
else:
    print("The word " + string + " is not a palindrome")