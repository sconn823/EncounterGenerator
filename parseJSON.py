import json
import requests

with open("monsters.json") as file:
    monsterList = json.load(file)

finishedList = []
for obj in monsterList["results"]:
    print(obj["url"])

    finishedList.append(
        {obj["name"]: requests.get(obj["url"]).content}
    )

with open("finishedList.json", "w") as output:
    json.dump(finishedList, output)
