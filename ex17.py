# # Exercise 17

# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage

import requests
from bs4 import BeautifulSoup

def scrapeNYT():
    titleList = []
    timesHTML = requests.get("https://www.nytimes.com/").text
    timesSoup = BeautifulSoup(timesHTML, 'lxml')
    timeH3 = timesSoup.find_all('h3')

    for item in timeH3:
        print(item.text, "\n")
        titleList.append(item.text)

def scrape15min():
    html = requests.get("https://www.15min.lt/")
    soup = BeautifulSoup(html.text, 'lxml')
    # for itemA in soup.find_all('h3', class_ = "template-field field-title field_title"):
    #     # for itemB in itemA.find_all('a'):
    #         print(itemA.text, "\n")

    for item in soup.find_all('h4'):
        print(item.contents[1].text, "\n")

scrape15min()




