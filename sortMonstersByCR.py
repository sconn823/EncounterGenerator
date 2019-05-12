import json
import requests

with open("monstersComplete.json", 'r') as inputFile:
    fullList = json.load(inputFile)

categorizedList = {
    0.125: [],
    0.25: [],
    0.5: [],
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: [],
    21: [],
    22: [],
    23: [],
    24: [],
    30: []
}
for obj in fullList:
    try:
        categorizedList[obj["challenge_rating"]].append(obj)
    except KeyError as e:
        print(e)

with open("crSortedMonsters.json", "w") as output:
    json.dump(categorizedList, output)
