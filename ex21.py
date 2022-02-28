# # Exercise 21

# Take the code from the How To Decode A Website exercise 
# (if you didn’t do it or just want to play with some different code, use the code from the solution), 
# and instead of printing the results to a screen, write the results to a txt file. 
# In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.


from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    timesHTML = requests.get("https://www.nytimes.com/").text
    timesSoup = BeautifulSoup(timesHTML, 'lxml')
    timeH3 = timesSoup.find_all('h3')
    
    name = str(input("What's the name of the file?")) + ".txt"

    with open(name, 'w', encoding="utf-8") as open_file:
        for item in timeH3:
            open_file.write(item.text + "\n")
        
