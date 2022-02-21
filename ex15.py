# # Exercise 15

# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 

# For example, say I type the string:
#   My name is Michele
# 
# Then I would see the string
#   Michele is name My

# shown back to me.

def reverseString(string): 
    return " ".join(string.split()[::-1])

sentence = str(input("Please input a sentence to be reversed: "))
print("This is your sentence reversed: ", reverseString(sentence))