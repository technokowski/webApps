__author__ = "technokowski"

import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.amazon.com/Nintendo-New-3DS-XL-Black/dp/B00S1LRX3W')
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "buyingPrice"})
print(element.text.strip())
# <span class="buyingPrice">194</span>

'''
 def ask_age():
    age = input("Enter your age: ")
    return int(age)

def calcuate_seconds_from_years(age_years):
    return age_years * 365 * 24 * 3600

def prompt_user_and_calculate_age():
    age = ask_age()
    seconds_lived = calcuate_seconds_from_years(age)
    print("You have lived for {} seconds".format(seconds_lived))
'''

#prompt_user_and_calculate_age()

