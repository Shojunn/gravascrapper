import requests
import sys
from art import tprint

##banner
tprint("GRAVASCRAPPER")
print("Gravatar passive data collection tool by Shojunn")
print()

##argument
handle = sys.argv[1]
print("=====INPUT=====")
print()
print("The input received was '" + handle + "'.")
print()
url = "https://www.gravatar.com/" + handle + ".json"
jasao = requests.get(url).json()

"""
##raw output
print("=====OUTPUT=====")
print()
print(jasao)
print()
"""

##refined output

print("=====OUTPUT=====")
print()

#id
if not jasao["entry"][0]["id"] != 0:
    print("ID: this field was left empty")
else:
    print("ID: " + jasao["entry"][0]["id"])

#username
if not jasao["entry"][0]["preferredUsername"] != 0:
    print("USERNAME: this field was left empty")
else:
    print("USERNAME: " + jasao["entry"][0]["preferredUsername"])

#name
if not jasao["entry"][0]["name"] != 0:
    print("NAME: this field was left empty")
else:
    print("NAME: " + str(jasao["entry"][0]["name"]["formatted"]))

#aboutme
if not jasao["entry"][0]["aboutMe"] != 0:
    print("BIO: this field was left empty")
else:
    print("BIO: " + jasao["entry"][0]["aboutMe"])

#urls
if len(jasao["entry"][0]["urls"]) <= 3:
    print("URL: this field was left empty")
else:
    print("URL (OPEN WITH CARE): " + str(jasao["entry"][0]["urls"]))

#thumbnailUrl
if not jasao["entry"][0]["thumbnailUrl"] != 0:
    print("Thumbnail: this field was left empty")
else:
    print("Thumbnail: " + jasao["entry"][0]["thumbnailUrl"])

print()
print("=====FINISHED=====")
print()



"""
try:
    print("USERNAME: " + jasao["entry"][0]["preferredUsername"])
except:
    print("Tone")

#type check
print(type(jasao["entry"]))
"""