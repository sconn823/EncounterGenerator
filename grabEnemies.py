import requests
import json

url = "http://www.dnd5eapi.co/api/monsters"

response = requests.get(url)

print(response.json())

with open("monsters.json", "w") as output:
    json.dump(response.json(), output)