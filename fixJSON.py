import requests
import json


with open('monsters.json', 'r') as inputFile:
    unParsedList = json.load(inputFile)

parsedList = []
for obj in unParsedList['results']:
    requestObj = requests.get(obj['url'])
    parsedList.append(requestObj.json())

with open("monstersComplete.json", "w") as output:
    json.dump(parsedList, output)
