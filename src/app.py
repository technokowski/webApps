__author__ = "technokowski"

import requests

request = requests.get("http://www.google.com")

def ask_age():
    age = input("Enter your age: ")
    return int(age)

def calcuate_seconds_from_years(age_years):
    return age_years * 365 * 24 * 3600

def prompt_user_and_calculate_age():
    age = ask_age()
    seconds_lived = calcuate_seconds_from_years(age)
    print("You have lived for {} seconds".format(seconds_lived))

#prompt_user_and_calculate_age()

print(request.content)