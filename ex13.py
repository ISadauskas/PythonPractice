# # Exercise 13

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonnaci(count):
    if count == 1:
        list = [1]
        return list
    elif count == 2:
        list = [1, 1]
        return list
    else:
        list = [1, 1]
        while count != 2:
            list.append(list[len(list) - 1] + list[len(list) - 2])
            count -= 1
        return list


num = int(input("Please input the ammount of fibonnaci you would like to be printed out: "))
print("Your fibonnaci sequence: ", fibonnaci(num))