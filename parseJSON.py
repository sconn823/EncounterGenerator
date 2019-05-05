import json
import requests


with open("monsters.json") as file:
    monsterList = json.load(file)

for obj in monsterList["results"]:
    print(obj)
