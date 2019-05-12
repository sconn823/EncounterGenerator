import requests
import json


with open('monsters.json', 'r') as inputFile:
    unParsedList = json.load(inputFile)

parsedList = []
for obj in unParsedList['results']:
    parsedList.append(obj)

print(len(parsedList))
