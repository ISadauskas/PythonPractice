# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import random
import string

def genPassword(type = "strong"):
    password = []
    if(type == "weak"):
        return random.choice(["bull", "bird", "time", "sun", "moon", "life", "stars", "table"])
    elif(type == "average"):
        for i in range(0, 8):
            password.append(random.choice(string.ascii_lowercase + string.digits))
        return "".join(password)
    else:
        for i in range(0, 12):
            password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        return "".join(password)


def genPass(length = 8, choice = string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(choice) for i in range(length))



type = str(input("How strong do you want your password to be: weak, average or strong? "))
while(type != "weak" and type != "average" and type != "strong"):
    type = str(input("How strong do you want your password to be: weak, average or strong? "))

print("Your password is: ", genPass(8))




