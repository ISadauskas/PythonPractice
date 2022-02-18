# # Exercise 15
#
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.

# Main program:

def reverse(string):
    return string[::-1]


string = input("Please input a string: ")
string = string.split()

print("Before reversing: " + str(string))
print("After reversing: " + str(reverse(string)))