import json
import random

groupRating = 10


def fixList(fullList, currentRating):
    newList = {}
    for number in fullList:
        if(float(number) <= currentRating):
            newList.update({number: fullList[number]})
    return newList


def findMonster(targetRating, monsterJSON):
    monsterOptions = []
    for obj in monsterJSON[targetRating]:
        monsterOptions.append(obj)

    chosenMonster = random.choice(monsterOptions)
    return(chosenMonster)


with open('crSortedMonsters.json', 'r') as input:
    sortedList = json.load(input)

sortedList = fixList(sortedList, groupRating)
challengeRatings = []
for obj in sortedList:
    if float(obj) > 0:
        challengeRatings.append(obj)

encounterList = []
while groupRating > 0:
    targetRating = random.choice(challengeRatings)
    encounterList.append(findMonster(targetRating, sortedList))
    groupRating -= float(targetRating)
    fixList(sortedList, groupRating)

sum = 0
for obj in encounterList:
    print(obj['name'] + " / " + str(obj['challenge_rating']))
    sum += float(obj['challenge_rating'])

print("Final rating: " + str(sum))
