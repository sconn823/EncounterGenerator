import json
import random

groupRating = 15


def fixList(fullList, currentRating):
    newList = []
    for number in fullList:
        if(float(number) <= currentRating):
            newList.append(number)
    return newList


def findMonster(targetRating, monsterJSON):
    monsterOptions = []
    for obj in monsterJSON[targetRating]:
        monsterOptions.append(obj)

    chosenMonster = random.choice(monsterOptions)
    return(chosenMonster)


with open('crSortedMonsters.json', 'r') as input:
    sortedList = json.load(input)


challengeRatings = []
for obj in sortedList:
    if float(obj) < groupRating and float(obj) != 0:
        challengeRatings.append(obj)

encounterList = []
while groupRating > 0:
    targetRating = random.choice(challengeRatings)
    encounterList.append(findMonster(targetRating, sortedList))
    groupRating -= float(targetRating)
    challengeRatings = fixList(challengeRatings, groupRating)

sum = 0
for obj in encounterList:
    print(obj['name'] + " / " + str(obj['challenge_rating']))
    sum += float(obj['challenge_rating'])

print("Final rating: " + str(sum))
