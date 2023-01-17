import requests
import sys
from art import tprint

#banner
tprint("GRAVASCRAPPER")
print("Gravatar passive data collection tool by Shojunn")
print()

#argument
handle = sys.argv[1]
print("=====INPUT=====")
print("The input received was" + handle)
print()
url = "https://www.gravatar.com/" + handle + ".json"
jasao = requests.get(url).json()

#output
print("=====OUTPUT=====")
print(jasao)