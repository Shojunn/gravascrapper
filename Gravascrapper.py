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
print("The input received was " + handle)
print()
url = "https://www.gravatar.com/" + handle + ".json"
jasao = requests.get(url).json()

#raw output
print("=====OUTPUT=====")
print(jasao)
print()

#refined output

##ALTERNATIVE
print("=====OUTPUT=====")
if not jasao["entry"][0]["preferredUsername"] != 0:
    print("USERNAME: this field is empty")
else:
    print("USERNAME: " + jasao["entry"][0]["preferredUsername"])

##TRY-EXCEPT
try:
    print("USERNAME: " + jasao["entry"][0]["preferredUsername"])
except:
    print("Tone")

#type check
print(type(jasao["entry"]))