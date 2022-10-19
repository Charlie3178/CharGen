from pickle import FALSE
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
import math
import random
import json

print(" 1. Barbarian")
print(" 2. Bard")
print(" 3. Cleric")
print(" 4. Druid")
print(" 5. Fighter")
print(" 6. Monk")
print(" 7. Paladin")
print(" 8. Ranger")
print(" 9. Rogue")
print(" 10. Sorcerer")
print(" 11. Warlock")
print(" 12. Wizard")

classChoice = int(input(" Please select a class  by entering a number from above: "))
LevelSelect = int(input(" Please choose a level between 1 and 20: "))

if LevelSelect > 0 and LevelSelect < 20:
    print("You have chosen a LV: ",LevelSelect,)
    if classChoice == 1:
        with open(".\ClassFilez\Barbarian.json") as BarbarianData:
            BarbarianClass = json.load(BarbarianData)
        # data = BarbarianClass['1']
        for i in BarbarianClass['Barbarian']:
            print("Class: ", i['1'])
            print("Hit Die: ", i['Hitdie'])
            print( i['Armor'])
            print( i['Weapons'])
            print( i['Saves'])
        BarbarianData.close
        
    elif classChoice == 2:
        BardData = open(".\ClassFilez\Bard.json")
        BardClass = json.load(BardData)
        BardData.close

        print(BardClass.items())
    elif classChoice == 3:
        ClericData = open(".\ClassFilez\Cleric.json")
        ClericClass = json.load(ClericData)
        ClericData.close

        print(ClericClass.items())
    elif classChoice == 4:
        DruidData = open(".\ClassFilez\Druid.json")
        DruidClass = json.load(DruidData)
        DruidData.close

        print(DruidClass.items())
    elif classChoice == 5:
        FighterData = open(".\ClassFilez\Fighter.json")
        FighterClass = json.load(FighterData)
        FighterData.close

        print(FighterClass.items())
    elif classChoice == 6:
        MonkData = open(".\ClassFilez\Monk.json")
        MonkClass = json.load(MonkData)
        MonkData.close

        print(MonkClass.items())
    elif classChoice == 7:
        PaladinData = open(".\ClassFilez\Paladin.json")
        PaladinClass = json.load(PaladinData)
        PaladinData.close

        print(PaladinClass.items())
    elif classChoice == 8:
        RangerData = open(".\ClassFilez\Ranger.json")
        RangerClass = json.load(RangerData)
        RangerData.close

        print(RangerClass.items())
    elif classChoice == 9:
        RogueData = open(".\ClassFilez\Rogue.json")
        RogueClass = json.load(RogueData)
        RogueData.close
        print(RogueClass.items())
    elif classChoice == 10:
        SorcererData = open(".\ClassFilez\Sorcerer.json")
        SorcererClass = json.load(SorcererData)
        SorcererData.close
        print(SorcererClass.items())
    elif classChoice == 11:
        WarlockData = open(".\ClassFilez\Warlock.json")
        WarlockClass = json.load(WarlockData)
        WarlockData.close
        print(WarlockClass.items())
    elif classChoice == 12:
        with open(".\ClassFilez\Wizard.json") as WizardData:
            WizardClass = json.load(WizardData)
        # print(WizardClass.items())
        # for (k, v) in WizardClass.items():
        #     print("Key: " + k, "Value: " + str(v), "\n")
        j = 0
        k = 0
        for i in WizardClass:
            print(j+1,": ",WizardClass[i])
            j += 1
            k += 1
            print(WizardClass[i][k])
        
        WizardData.close

