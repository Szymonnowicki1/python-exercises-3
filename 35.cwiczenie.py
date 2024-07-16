# -*- coding: utf-8 -*-
import random
from enum import Enum

Event = Enum('Event', ['chest', 'nothing'])

Colours = Enum('Colours', {'green' : 'zielony', 'orange' : 'pomaranczowy', 'purple' : 'fioletowy', 'gold' : 'zloty'}


               

chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }
chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())


gameLenght = 0
goldAcquired = 0

EventDictionary = {Event.chest : 60, Event.nothing : 40}
EventList = list(eventDictionary.keys())
EventPropability = list(eventDictionary.values())

rewardForChest = {'green' : 1000, 'orange' : 4000, 'purple' : 9000, 'gold' : 16000}

print('welcome in game KOMNATA')
print('you have only 5 steps to see how many gold you earned')

while gameLenght < 5:
    gameLenght = gameLenght + 1
    gamerAnswer = input('do you wanan go forward :')
    if gamerAnswer == 'yes':
        print('nice lets se what you got')
        drawnEvent = random.choices(EventList, EventPropability)[0]
        if (drawnEvent == Event.chest):
            print('great job you have got a chest')
            drawnColour = random.choices(ChestColourList, ChestColourProbability)[0]
            print('the chest colour is', drawnColour.values )
            gamerReward = rewardForChest[drawnColour]
            goldAcquired = goldAcquired + gamerReward
        elif (drawnEvent == Event.nothing):
            print('unfortunetlly you are so unlucky :(')
    else:
        print('sry you can go only forward')
    continue



# %%
import random
from enum import Enum

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())


Colours = Enum('Colours', {'Green': 'zielony',
                           'Orange': 'pomarańczowy',
                           'Purple': 'fiolet',
                           'Gold': 'złoty'
                          }
               )

chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }
chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
                       chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                       for reward in range(len(chestColourList))
                   }

gameLength = 5
goldAcquired = 0

print("Welcome in my game called KOMNATA")
print("""You have only 5 steps to make,
see yourself how much gold you gonna acquire till the end!""")

while gameLength > 0:
    gamerAnswer = input("Do you want to move forward?")
    if (gamerAnswer == "yes"):
        print("Great, let's see what you got...")
        drawnEvent = random.choices(eventList,eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("You've drawn a CHEST")
            drawnColour = random.choices(chestColourList,chestColourProbability)[0]
            print("The chest color is", drawnColour.value)
            gamerReward = rewardsForChests[drawnColour]
            goldAcquired = goldAcquired + gamerReward
        elif(drawnEvent == Event.Empty):
            print("You've drawn nothing, you are so unlucky!")
            
    else:
        print("You can go just straight man, nothing else, this game is dumb")
        continue
    
    gameLength = gameLength - 1

print("Congratulation, you have acquired: ", goldAcquired)
