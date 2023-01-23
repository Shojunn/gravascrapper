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

##existence check

if jasao == "User not found":
    print("=====OUTPUT=====")
    print()
    print("This username is not tied to a Gravatar account.")
    print()
else:

    """
    ##raw output
    print("=====OUTPUT=====")
    print()
    print(jasao)
    print()
    """

    ##refined output

    print("=====BIOGRAPHIC OUTPUT=====")
    print()

    #id
    if not jasao["entry"][0]["id"] != 0:
        print("ID: ---")
    else:
        print("ID: " + jasao["entry"][0]["id"])

    #username
    if not jasao["entry"][0]["preferredUsername"] != 0:
        print("USERNAME: ---")
    else:
        print("USERNAME: " + jasao["entry"][0]["preferredUsername"])

    #displayName

    try:
        if not jasao["entry"][0]["displayName"] != 0:
            print("DISPLAY NAME: ---")
        else:
            print("DISPLAY NAME: " + jasao["entry"][0]["displayName"])
    except:
        print("DISPLAY NAME: ---")

    #name
    try:
        if not jasao["entry"][0]["name"] != 0:
            print("NAME: ---")
        else:
            print("NAME: " + str(jasao["entry"][0]["name"]["formatted"]))
    except:
        print("NAME: ---")

    #aboutme
    try:
        if not jasao["entry"][0]["aboutMe"] != 0:
            print("BIO: ---")
        else:
            print("BIO: " + jasao["entry"][0]["aboutMe"])
    except:
        print("BIO: ---")

    #currentLocation
    try:
        if not jasao["entry"][0]["currentLocation"] != 0:
            print("LOCATION: ---")
        else:
            print("LOCATION: " + jasao["entry"][0]["currentLocation"])
    except:
        print("LOCATION: ---")

    print()
    print("=====EMAIL & URLS=====")
    print()

    #emails
    try:
        if not jasao["entry"][0]["emails"][0]["value"] != 0:
            print("EMAIL: ---")
        else:
            print("EMAIL: " + jasao["entry"][0]["emails"][0]["value"])
    except:
        print("EMAIL: ---")

    #urls
    try:
        if len(jasao["entry"][0]["urls"]) >= 2:
            print("URL: ---")
        else:
            print("URL (OPEN WITH CARE): " + str(jasao["entry"][0]["urls"][0]["value"]))
    except:
        print("URL: ---")

    #thumbnailUrl
    try:
        if not jasao["entry"][0]["thumbnailUrl"] != 0:
            print("THUMBNAIL URL: ---")
        else:
            print("THUMBNAIL URL: " + jasao["entry"][0]["thumbnailUrl"])
    except:
        print("THUMBNAIL URL: ---")
    
    #profileBackground'
    try:
        if not jasao["entry"][0]["profileBackground"]["url"] != 0:
            print("BACKGROUND: ---")
        else:
            print("BACKGROUND: " + jasao["entry"][0]["profileBackground"]["url"])
    except:
        print("BACKGROUND: ---")

    print()
    print("=====ACCOUNTS=====")
    print()

    #ims-Skype
    try:
        if not jasao["entry"][0]["ims"][0]["value"] != 0:
            print("SKYPE: ---")
        else:
            print("SKYPE: " + jasao["entry"][0]["ims"][0]["value"])
    except:
        print("SKYPE: ---")

    #twitter
    try:
        if not jasao["entry"][0]["accounts"][0]["url"] != 0:
            print("TWITTER: ---")
        else:
            print("TWITTER: " + jasao["entry"][0]["accounts"][0]["url"])
    except:
        print("TWITTER: ---")

    print()
    print("=====FINISHED=====")
    print()
