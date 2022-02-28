# # Exercise 19

# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: 
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

# The article is long, so it is split up between 4 pages. 
# Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

from urllib import request
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    html = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture").text
    soup = BeautifulSoup(html, 'lxml')
    
    for par in soup.find_all('p'):
        print(par.text, "\n")
