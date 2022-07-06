import json
import random
import string
import time
import validators

def JsonText(input) -> str:
    return json.dumps(input)

def ValidUrl(input: str):
    return validators.url(input)

def GenerateCode(length: int) -> str:
    charsForCode = string.ascii_letters + string.digits
    return ''.join(random.choice(charsForCode) for _ in range(length))


def GetInfo(code: str):
    with open("urls.json", "r", errors="ignore") as jsonFile:
        urlsDatabase = json.load(jsonFile)
    if (code in urlsDatabase):
        return [True, urlsDatabase[code]]
    else:
        return [False, None]

def RemoveCode(code: str) -> None:
    with open("urls.json", "r", errors="ignore") as jsonFile:
        urlsDatabase = json.load(jsonFile)
        urlsDatabase.pop(code, None)
    with open("urls.json", "w", errors="ignore") as jsonFile:
        json.dump(urlsDatabase, jsonFile)

def CreateUrl(code: str, url: str) -> None:
    with open("urls.json", "r", errors="ignore") as jsonFile:
        urlsDatabase = json.load(jsonFile)
        urlsDatabase[code] = {"url": url, "timestamp": round(time.time())}
    with open("urls.json", "w", errors="ignore") as jsonFile:
        json.dump(urlsDatabase, jsonFile)

def CheckCode(code: str):
    with open("urls.json", "r", errors="ignore") as jsonFile:
        urlsDatabase = json.load(jsonFile)
    if (code in urlsDatabase):
        return [True, urlsDatabase[code]["url"]]
    return [False, None]

def GetUrl(link: str):
    with open("urls.json", "r", errors="ignore") as jsonFile:
        urlsDatabase = json.load(jsonFile)
    for each in urlsDatabase:
        if urlsDatabase[each]["url"] == link:
            return [True, each]
    return [False, None]