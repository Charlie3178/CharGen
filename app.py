import math
from operator import concat
import os
from pyexpat import features
import random

pname = ""
strength = 0
strmod = 0
dexterity = 0
dexmod = 0
constitution = 0
conmod = 0
intelligence = 0
intmod = 0
wisdom = 0
wismod = 0
charisma = 0
chamod = 0
hp = 0
race = ""
stradjust = 0
dexadjust = 0
conadjust = 0
intadjust = 0
wisadjust = 0
chaadjust = 0
spellz = ""
again = ""
while again != "n":
    strength = random.randint(10,18)
    strmod = math.floor((strength - 10)/2)
    dexterity = random.randint(10,18)
    dexmod = math.floor((dexterity - 10)/2)
    constitution = random.randint(10,18)
    conmod = math.floor((constitution - 10)/2)
    intelligence = random.randint(10,18)
    intmod = math.floor((intelligence - 10)/2)
    wisdom = random.randint(10,18)
    wismod = math.floor((wisdom - 10)/2)
    charisma = random.randint(10,18)
    chamod = math.floor((charisma - 10)/2)
    print("\nStrength: ",strength,"\n","Dexterity: ",dexterity,"\n","Constitution: ",constitution,"\n","Intelligence: ",intelligence,"\n","Wisdom: ",wisdom,"\n","Charisma: ",charisma)
    again = input("Woul you like to re-roll? (y or n) : ")
    if again.lower() != "n":
        again = "y"
        os.system("cls")

#######################################
#######################################
def playerStats():
    pname = input(" Please name your character: ")
    gender = input(" What gender is your character?: ")
    def pRace():
        print(" 1. Hill Dwarf")
        print(" 2. Mountain Dwarf")
        print(" 3. High Elf")
        print(" 4. Wood Elf")
        print(" 5. Drow")
        print(" 6. Lightfoot Halfling")
        print(" 7. Stout Halfling")
        print(" 8. Human")
        print(" 9. Dragonborn")
        print(" 10. Forest Gnome")
        print(" 11. Rock Gnome")
        print(" 12. Half-Elf")
        print(" 13. Half-Orc")
        print(" 14. Tiefling")
        racechoice = int(input(" Please choose a race by entering a number from above: "))
        if racechoice == 1:
            race = "Hill Dwarf"
            racetraits = ["Speed 25ft: Not encumbered by wearing heavy armor","Darkvision","Advantage on saving throws against poison","Resistance to poison damage","Battleaxe, Handaxe, Throwing Hammer, Warhammer","+1 HP/lv", "Choose an Artisan Toolset: Smith's Tools, Brewers Supplies, Mason's Tools","Stone Cunning"]
            strAdjust = 0
            dexAdjust = 0
            conAdjust = 2
            intAdjust = 0
            wisAdjust = 1
            chaAdjust = 0
        elif racechoice == 2:
            race = "Mountain Dwarf"
            racetraits = ["Speed 25ft: Not encumbered by wearing heavy armor","Darkvision","Advantage on saving throws against poison","Resistance to poison damage","Battleaxe, Handaxe, Throwing Hammer, Warhammer","Light and Medium Armor", "Choose an Artisan Toolset: Smith's Tools, Brewers Supplies, Mason's Tools","Stone Cunning"]
            strAdjust = 2
            dexAdjust = 0
            conAdjust = 2
            intAdjust = 0
            wisAdjust = 0
            chaAdjust = 0
        elif racechoice == 3:
            race = "High Elf"
            racetraits = ["Longsword","Shorsword","Longbow","Shortbow","Darkvision","Keen Senses","Advantage against being charmed","Immune to magical sleep","Trance","1 Wizard Cantrip","1 bonus language"]
            strAdjust = 0
            dexAdjust = 2
            conAdjust = 0
            intAdjust = 1
            wisAdjust = 0
            chaAdjust = 0
        elif racechoice == 4:
            race = "Wood Elf"
            racetraits = ["Longsword","Shorsword","Longbow","Shortbow","Darkvision","Keen Senses","Advantage against being charmed","Immune to magical sleep","Trance","Speed 35ft","Mask of the Wild"]
            strAdjust = 0
            dexAdjust = 2
            conAdjust = 0
            intAdjust = 0
            wisAdjust = 1
            chaAdjust = 0
        elif racechoice == 5:
            race = "Drow"
            racetraits = ["Longsword, Shorsword, Longbow, Shortbow","Superior Darkvision","Keen Senses","Advantage against being charmed","Immune to magical sleep","Trance","Sunlight Sensativity","Rapier, Hand Crossbow"]
            strAdjust = 0
            dexAdjust = 2
            conAdjust = 0
            intAdjust = 0
            wisAdjust = 0
            chaAdjust = 1
        elif racechoice == 6:
            race = "Lightfoot Halfling"
            racetraits = ["Speed 25ft","Lucky","Brave","Halfling Nimbleness","Naturally Stealthy"]
            strAdjust = 0
            dexAdjust = 2
            conAdjust = 0
            intAdjust = 0
            wisAdjust = 0
            chaAdjust = 1
        elif racechoice == 7:
            race = "Stout Halfling"
            racetraits = ["Speed 25ft","LLucky","Brave","Halfling Nimbleness","Stout Resilience"]
            strAdjust = 0
            dexAdjust = 2
            conAdjust = 1
            intAdjust = 0
            wisAdjust = 0
            chaAdjust = 0
        elif racechoice == 8:
            race = "Human"
            racetraits = []
            strAdjust = 1
            dexAdjust = 1
            conAdjust = 1
            intAdjust = 1
            wisAdjust = 1
            chaAdjust = 1
        elif racechoice == 9:
            race = "Dragonborn"
            racetraits = ["Draconic Ancestry", "Breath Weapon","Damage Resistance","Draconic, Common"]
            strAdjust = 2
            dexAdjust = 0
            conAdjust = 0
            intAdjust = 0
            wisAdjust = 0
            chaAdjust = 1
        elif racechoice == 10:
            race = "Forest Gnome"
            racetraits = ["Speed 25ft","Darkvision","Gnome Cunning","Natural Illusionist","Speak with Beasts"]
            strAdjust = 0
            dexAdjust = 1
            conAdjust = 0
            intAdjust = 2
            wisAdjust = 0
            chaAdjust = 0
        elif racechoice == 11:
            race = "Rock Gnome"
            racetraits = ["Speed 25ft","Darkvision","Gnome Cunning","Artificer's Lore","Tinker","Common, Gnomish"]
            strAdjust = 0
            dexAdjust = 0
            conAdjust = 1
            intAdjust = 2
            wisAdjust = 0
            chaAdjust = 0
        elif racechoice == 12:
            race = "Half-Elf"
            racetraits = ["Darkvision","Fey Ancestry","Skill Versatility","Common, Elvish, Bonus Language"]
            strAdjust = 0
            dexAdjust = 0
            conAdjust = 0
            intAdjust = 0
            wisAdjust = 0
            chaAdjust = 2
        elif racechoice == 13:
            race = "Half-Orc"
            racetraits = ["Darkvision","Menacing","Relentless Endurance","Savage Attacks","Common, Orcish"]
            strAdjust = 2
            dexAdjust = 0
            conAdjust = 1
            intAdjust = 0
            wisAdjust = 0
            chaAdjust = 0
        elif racechoice == 14:
            race = "Tiefling"
            racetraits = ["Darkvision","Hellish Resistance","Common, Infernal"]
            strAdjust = 0
            dexAdjust = 0
            conAdjust = 0
            intAdjust = 1
            wisAdjust = 0
            chaAdjust = 2    
        return(race,strAdjust,dexAdjust,conAdjust,intAdjust,wisAdjust,chaAdjust,racetraits)

    def Pclass():
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
        # print(" 13. Artificer")
        classChoice = int(input(" Please select a class  by entering a number from above: "))
        if classChoice == 1:
            playerClass = "Barbarian"
            hitdie = 12
            proficiency = 2
            armor = "Light and Medium"
            weapon = "Simple and Martial"
            shields = True
            saves = "Strength and Constitution"
            features = ["Rage 2/day", "Unarmored Def (10 + Dex modifier + Con modifier)"]
            toolz = "None"
            cantripz = []
            domain = []
            pact = []
            spellz = []
            sorOrig = []
            def skills():
                print(" 1. Animal Handling")
                print(" 2. Athletics")
                print(" 3. Intimidation")
                print(" 4. Nature")
                print(" 5. Perception")
                print(" 6. Survival")
                i = 0
                while i < 3:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Animal Handling")
                    elif skillchoice == 2:
                        skill = skill.append("Athletics")
                    elif skillchoice == 3:
                        skill = skill.append("Intimidation")
                    elif skillchoice == 4:
                        skill = skill.append("Nature")
                    elif skillchoice == 5:
                        skill = skill.append("Perception")
                    elif skillchoice == 6:
                        skill = skill.append("Survival")
                    i += 1
                return(skill)
            cskills = skills()
        elif classChoice == 2:
            playerClass = "Bard"
            hitdie = 8
            proficiency = 2
            armor = "Light"
            weapon = "Simple Weapons,Hand Crossbows,Longswords,Rapiers,Shortswords"
            shields = False
            saves = "Dexterity and Charisma"
            features = ["Bardic Inspiration (d6)", "Spellcasting"]
            toolz = "Three musical instruments of your choice"
            domain = []
            pact = []
            spellz = []
            sorOrig = []
            def kantripz():
                print(" 1. Blade Ward")
                print(" 2. Dancing Lights")
                print(" 3. Friends")
                print(" 4. Light")
                print(" 5. Mage Hand")
                print(" 6. Mending")
                print(" 7. Message")
                print(" 8. Minor Illusion")
                print(" 9. Prestidigitation")
                print(" 10. True Strike")
                print(" 11. Vicious Mockery")
                print(" You get 2 Cantrips to start.")
                cantrip1 = input(" Please choose your first cantrip by entering the name from above: ")
                cantrip2 = input(" Please choose your second cantrip by entering the name from above: ")
                return(cantrip1,cantrip2)
            cantripz = kantripz()
            def skills():
                print(" 1. Acrobatics")
                print(" 2. Animal Handling")
                print(" 3. Arcana")
                print(" 4. Athletics")
                print(" 5. Deception")
                print(" 6. History")
                print(" 7. Insight")
                print(" 8. Intimidation")
                print(" 9. Investigation")
                print(" 10. Medicine")
                print(" 11. Nature")
                print(" 12. Perception")
                print(" 13. Performance")
                print(" 14. Persuasion")
                print(" 15. Religion")
                print(" 16. Sleight of Hand")
                print(" 17. Stealth")
                print(" 18. Survival")
                print(" You get 3 Skills.")
                i = 0
                while i < 3:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the number from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Acrobatics")
                    elif skillchoice == 2:
                        skill = skill.append("Animal Handling")
                    elif skillchoice == 3:
                        skill = skill.append("Arcana")
                    elif skillchoice == 4:
                        skill = skill.append("Athletics")
                    elif skillchoice == 5:
                        skill = skill.append("Deception")
                    elif skillchoice == 6:
                        skill = skill.append("History")
                    elif skillchoice == 7:
                        skill = skill.append("Insight")
                    elif skillchoice == 8:
                        skill = skill.append("Intimidation")
                    elif skillchoice == 9:
                        skill = skill.append("Investigation")
                    elif skillchoice == 10:
                        skill = skill.append("Medicine")
                    elif skillchoice == 11:
                        skill = skill.append("Nature")
                    elif skillchoice == 12:
                        skill = skill.append("Perception")
                    elif skillchoice == 13:
                        skill = skill.append("Performance")
                    elif skillchoice == 14:
                        skill = skill.append("Persuasion")
                    elif skillchoice == 15:
                        skill = skill.append("Religion")
                    elif skillchoice == 16:
                        skill = skill.append("Slieght of Hand")
                    elif skillchoice == 17:
                        skill = skill.append("Stealth")
                    elif skillchoice == 18:
                        skill = skill.append("Survival")
                    i += 1
                return(skill)
            cskills = skills()
            def SpellSelection():
                print("  1. Animal Friendship")
                print("  2. Bane")
                print("  3. Charm Person")
                print("  4. Comprehend Languages")
                print("  5. Cure Wounds")
                print("  6. Detect Magic")
                print("  7. Disguise Self")
                print("  8. Dissonant Whispers")
                print("  9. Faerie Fire")
                print(" 10. Feather Fall")
                print(" 11. Healing Word")
                print(" 12. Heroism")
                print(" 13. Identify")
                print(" 14. Illusory Script")
                print(" 15. Longstrider")
                print(" 16. Silent Image")
                print(" 17. Sleep")
                print(" 18. Speak with Animals")
                print(" 19. Tasha’s Hideous Laughter")
                print(" 20. Thunderwave")
                print(" 21. Unseen Servant")
                i = wismod + 1
                level1spells = []
                while i > 0:
                    spellconcat1 = (concat("Please select ",str(i)))
                    spellconcat2 = (concat(spellconcat1," more spells: "))
                    spellchoice = int(input(spellconcat2))
                    if spellchoice == 1:
                        level1spells.append("Animal Friendship")
                    elif spellchoice == 2:
                        level1spells.append("Bane")
                    elif spellchoice == 3:
                        level1spells.append("Charm Person")
                    elif spellchoice == 4:
                        level1spells.append("Comprehend Languages")
                    elif spellchoice == 5:
                        level1spells.append("Cure Wounds")
                    elif spellchoice == 6:
                        level1spells.append("Detect Magic")
                    elif spellchoice == 7:
                        level1spells.append("Disguise Self")
                    elif spellchoice == 8:
                        level1spells.append("Dissonant Whispers")
                    elif spellchoice == 9:
                        level1spells.append("Faerie Fire")
                    elif spellchoice == 10:
                        level1spells.append("Feather Falld")
                    elif spellchoice == 11:
                        level1spells.append("Healing Word")
                    elif spellchoice == 12:
                        level1spells.append("Heroism")
                    elif spellchoice == 13:
                        level1spells.append("Identify")
                    elif spellchoice == 14:
                        level1spells.append("Illusory Script")
                    elif spellchoice == 15:
                        level1spells.append("Longstrider")
                    elif spellchoice == 16:
                        level1spells.append("Silent Image")
                    elif spellchoice == 17:
                        level1spells.append("Sleep")
                    elif spellchoice == 18:
                        level1spells.append("Speak with Animals")
                    elif spellchoice == 19:
                        level1spells.append("Tasha’s Hideous Laughter")
                    elif spellchoice == 20:
                        level1spells.append("Thunderwave")
                    elif spellchoice == 21:
                        level1spells.append("Unseen Servant")
                    i -= 1
                return(level1spells)
            spellz = SpellSelection()
        elif classChoice == 3:
            playerClass = "Cleric"
            hitdie = 8
            proficiency = 2
            armor = "Light and Medium"
            weapon = "Simple Weapons"
            shields = True
            saves = "Wisdm and Charisma"
            toolz = "None"
            features = ["Spellcasting", "Divine Domain"]
            spellz = []
            sorOrig = []
            pact = []
            def kantripz():
                print(" 1. Guidance")
                print(" 2. Light")
                print(" 3. Mending")
                print(" 4. Resistance")
                print(" 5. Sacred Flame")
                print(" 6. Spare the Dying")
                print(" 7. Thaumaturgy")
                print(" You get 3 Cantrips to start.")
                cantrip1 = input(" Please choose your first cantrip by entering the name from above: ")
                cantrip2 = input(" Please choose your second cantrip by entering the name from above: ")
                cantrip3 = input(" Please choose your third cantrip by entering the name from above: ")
                return(cantrip1,cantrip2,cantrip3)
            cantripz = kantripz()
            def skills():
                print(" 1. Insight")
                print(" 2. Medicine")
                print(" 3. Persuasion")
                print(" 4. Religion")
                print(" You get 2 Skills.")
                i = 0
                while i < 2:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Insight")
                    elif skillchoice == 2:
                        skill = skill.append("Medicine")
                    elif skillchoice == 3:
                        skill = skill.append("Persuasion")
                    elif skillchoice == 4:
                        skill = skill.append("Religion")
                    i += 1                
                return(skill)
            cskills = skills()
            def divdomain():
                print(" 1. Knowledge")
                print(" 2. Life")
                print(" 3. Light")
                print(" 4. Nature")
                print(" 5. Tempest")
                print(" 6. Trickery")
                print(" 7. War")
                domainSpell1 = ""
                domainSpell2 = ""
                domainCoice = input(" Please choose one domain by entering the name from the list above: ")
                if domainCoice == "Knowledge":
                    domainSpell1= "Command"
                    domainSpell2= "Identify"
                elif domainCoice == "Life":
                    domainSpell1 = "Bless" 
                    domainSpell2 ="Cure Wounds"
                elif domainCoice == "Light":
                    domainSpell1 = "Burning Hands"
                    domainSpell2 = "Faerie Fire"
                elif domainCoice == "Nature":
                    domainSpell1 = "Animal Friendship"
                    domainSpell2 = "Speak with Animals"
                elif domainCoice == "Tempest":
                    domainSpell1 = "Fog Cloud"
                    domainSpell2 = "Thunderwave"
                elif domainCoice == "Trickery":
                    domainSpell1 = "Charm Person"
                    domainSpell2 = "Disguise Self"
                elif domainCoice == "War":
                    domainSpell1 = "Divine Favor"
                    domainSpell2 = "Shield of Faith"
                return(domainCoice,domainSpell1,domainSpell2)
            domain = divdomain()
            def SpellSelection():
                print("  1. Bane")
                print("  2. Bless")
                print("  3. Command")
                print("  4. Create or Destroy Water")
                print("  5. Cure Wounds")
                print("  6. Detect Evil and Good")
                print("  7. Detect Magic")
                print("  8. Detect Poison and Disease")
                print("  9. Guiding Bolt")
                print(" 10. Healing Word")
                print(" 11. Inflict Wounds")
                print(" 12. Protection from Evil and Good")
                print(" 13. Purify Food and Drink")
                print(" 14. Sanctuary")
                print(" 15. Shield of Faith")
                i = wismod + 1
                level1spells = []
                while i > 0:
                    spellconcat1 = (concat("Please select ",str(i)))
                    spellconcat2 = (concat(spellconcat1," more spells: "))
                    spellchoice = int(input(spellconcat2))
                    if spellchoice == 1:
                        level1spells.append("Bane")
                    elif spellchoice == 2:
                        level1spells.append("Bless")
                    elif spellchoice == 3:
                        level1spells.append("Command")
                    elif spellchoice == 4:
                        level1spells.append("Create or Destroy Water")
                    elif spellchoice == 5:
                        level1spells.append("Cure Wounds")
                    elif spellchoice == 6:
                        level1spells.append("Detect Evil and Good")
                    elif spellchoice == 7:
                        level1spells.append("Detect Magic")
                    elif spellchoice == 8:
                        level1spells.append("Detect Poison and Disease")
                    elif spellchoice == 9:
                        level1spells.append("Guiding Bolt")
                    elif spellchoice == 10:
                        level1spells.append("Healing Word")
                    elif spellchoice == 11:
                        level1spells.append("Inflict Wounds")
                    elif spellchoice == 12:
                        level1spells.append("Protection from Evil and Good")
                    elif spellchoice == 13:
                        level1spells.append("Purify Food And Drink")
                    elif spellchoice == 14:
                        level1spells.append("Sanctuary")
                    elif spellchoice == 15:
                        level1spells.append("Shield of Faith")
                    i -= 1
                return(level1spells)
            spellz = SpellSelection()
        elif classChoice == 4:
            playerClass = "Druid"
            hitdie = 8
            proficiency = 2
            armor = "Light and Medium -Druids will not wear armor or shields made of metal"
            weapon = "Clubs, Daggers, Darts, Javelins, Maces, Quarterstaffs, Scimitars, Slings, Spears"
            shields = True
            saves = "Intelligence and Wisdom"
            toolz = "Herbalism Kit"
            features = ["Druidic", "Spellcasting"]
            spellz = []
            pact = []
            sorOrig = []
            domain = []
            def kantripz():
                print(" 1. Druidcraft")
                print(" 2. Guidance")
                print(" 3. Mending")
                print(" 4. Poison Spray")
                print(" 5. Produce Flame")
                print(" 6. Resistance")
                print(" 7. Shillelagh")
                print(" 8. Thorn Whip")
                print(" You get 2 Cantrips to start.")
                cantrip1 = input(" Please choose your first cantrip by entering the name from above: ")
                cantrip2 = input(" Please choose your second cantrip by entering the name from above: ")
                return(cantrip1,cantrip2)
            cantripz = kantripz()
            def skills():
                print(" 1. Arcana")
                print(" 2. Animal Handling")
                print(" 3. Insight")
                print(" 4. Medicine")
                print(" 5. Nature")
                print(" 6. Perception")
                print(" 7. Religion")
                print(" 8. Survival")
                print(" You get 2 Skills.")
                i = 0
                while i < 2:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Arcana")
                    elif skillchoice == 2:
                        skill = skill.append("Animal Handling")
                    elif skillchoice == 3:
                        skill = skill.append("Insight")
                    elif skillchoice == 4:
                        skill = skill.append("Medicine")
                    elif skillchoice == 5:
                        skill = skill.append("Nature")
                    elif skillchoice == 6:
                        skill = skill.append("Perception")
                    elif skillchoice == 7:
                        skill = skill.append("Religion")
                    elif skillchoice == 8:
                        skill = skill.append("Survival")
                    i += 1
                return(skill)
            cskills = skills()

            def SpellSelection():
                print("  1. Animal Friendship")
                print("  2. Charm Person")
                print("  3. Create or Destroy Water")
                print("  4. Cure Wounds")
                print("  5. Detect Magic")
                print("  6. Detect Poison and Disease")
                print("  7. Entangle")
                print("  8. Faerie Fire")
                print("  9. Fog Cloud")
                print(" 10. Goodberry")
                print(" 11. Healing Word")
                print(" 12. Jump")
                print(" 13. Longstrider")
                print(" 14. Purify Food and Drink")
                print(" 15. Speak with Animals")
                print(" 16. Thunderwave")
                i = wismod + 1
                level1spells = []
                while i > 0:
                    spellconcat1 = (concat("Please select ",str(i)))
                    spellconcat2 = (concat(spellconcat1," more spells: "))
                    spellchoice = int(input(spellconcat2))
                    if spellchoice == 1:
                        level1spells.append("Animal Friendship")
                    elif spellchoice == 2:
                        level1spells.append("Charm Person")
                    elif spellchoice == 3:
                        level1spells.append("Create or Destroy Water")
                    elif spellchoice == 4:
                        level1spells.append("Cure Wounds")
                    elif spellchoice == 5:
                        level1spells.append("Detect Magic")
                    elif spellchoice == 6:
                        level1spells.append("Detect Poison and Disease")
                    elif spellchoice == 7:
                        level1spells.append("Entangle")
                    elif spellchoice == 8:
                        level1spells.append("Faerie Fire")
                    elif spellchoice == 9:
                        level1spells.append("Fog Cloud")
                    elif spellchoice == 10:
                        level1spells.append("Goodberry")
                    elif spellchoice == 11:
                        level1spells.append("Healing Word")
                    elif spellchoice == 12:
                        level1spells.append("Jump")
                    elif spellchoice == 13:
                        level1spells.append("Longstrider")
                    elif spellchoice == 14:
                        level1spells.append("Purify Food and Drink")
                    elif spellchoice == 15:
                        level1spells.append("Speak with Animals")
                    elif spellchoice == 16:
                        level1spells.append("Thunderwave")
                    i -= 1
                return(level1spells)
            spellz = SpellSelection()

            domain = []
        elif classChoice == 5:
            playerClass = "Fighter"
            hitdie = 10
            proficiency = 2
            armor = "All Armor"
            weapon = "Simple and Martial"
            shields = True
            saves = "Strength and Constitution"
            toolz = "None"
            features = ["Fighting Style", "Second Wind"]
            cantripz = []
            spellz = []
            pact = []
            sorOrig = []
            domain = []
            def skills():
                print(" 1. Acrobatics")
                print(" 2. Animal Handling")
                print(" 3. Athletics")
                print(" 4. History")
                print(" 5. Insight")
                print(" 6. Intimidation")
                print(" 7. Perception")
                print(" 8. Survival")
                print(" You get 2 Skills.")
                i = 0
                while i < 2:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Acrobatics")
                    elif skillchoice == 2:
                        skill = skill.append("Animal Handling")
                    elif skillchoice == 3:
                        skill = skill.append("Athletics")
                    elif skillchoice == 4:
                        skill = skill.append("History")
                    elif skillchoice == 5:
                        skill = skill.append("Insight")
                    elif skillchoice == 6:
                        skill = skill.append("Intimidation")
                    elif skillchoice == 7:
                        skill = skill.append("Perception")
                    elif skillchoice == 8:
                        skill = skill.append("Survival")
                    i += 1
                # skill1 = input(" Please choose your first skill by entering the name from above: ")
                # skill2 = input(" Please choose your second skill by entering the name from above: ")
                return(skill)
            cskills = skills()
            domain = []
        elif classChoice == 6:
            playerClass = "Monk"
            hitdie = 8
            proficiency = 2
            armor = "None"
            weapon = "Simple Weapons and Shortswords"
            shields = False
            saves = "Strength and Dexterity"
            toolz = "Pick one Artisan's Tool Kit or Musical Weapon"
            features = ["Unarmored Defense", "Martial Arts 1d4"]
            cantripz = []
            spellz = []
            pact = []
            domain = []
            sorOrig = []
            def skills():
                print(" 1. Acrobatics")
                print(" 2. Athletics")
                print(" 3. History")
                print(" 4. Insight")
                print(" 5. Religion")
                print(" 6. Stealth")
                print(" You get 2 Skills to start.")
                i = 0
                while i < 2:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Acrobatics")
                    elif skillchoice == 2:
                        skill = skill.append("Athletics")
                    elif skillchoice == 3:
                        skill = skill.append("History")
                    elif skillchoice == 4:
                        skill = skill.append("Insight")
                    elif skillchoice == 5:
                        skill = skill.append("Religion")
                    elif skillchoice == 6:
                        skill = skill.append("Stealth")
                    i += 1
                # skill1 = input(" Please choose your first skill by entering the name from above: ")
                # skill2 = input(" Please choose your second skill by entering the name from above: ")
                return(skill)
            cskills = skills()
            domain = []
        elif classChoice == 7:
            playerClass = "Paladin"
            hitdie = 10
            proficiency = 2
            armor = "All Armors"
            weapon = "Simple and Martial"
            shields = True
            saves = "Wisdom and Charisma"
            toolz = "None"
            features = ["Divine Sense", "Lay on Hands"]
            cantripz = []
            spellz = []
            pact = []
            domain = []
            sorOrig = []
            def skills():
                print(" 1. Athletics")
                print(" 2. Insight")
                print(" 3. Intimidation")
                print(" 4. Medicine")
                print(" 5. Persuasion")
                print(" 6. Religion")
                print(" You get 2 Skills to start.")
                i = 0
                while i < 2:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Athletics")
                    elif skillchoice == 2:
                        skill = skill.append("Insight")
                    elif skillchoice == 3:
                        skill = skill.append("Intimidation")
                    elif skillchoice == 4:
                        skill = skill.append("Mrdicine")
                    elif skillchoice == 5:
                        skill = skill.append("Persuasion")
                    elif skillchoice == 6:
                        skill = skill.append("Religion")
                    i += 1
                # skill1 = input(" Please choose your first skill by entering the name from above: ")
                # skill2 = input(" Please choose your second skill by entering the name from above: ")
                return(skill)
            cskills = skills()
            domain = []
        elif classChoice == 8:
            playerClass = "Ranger"
            hitdie = 10
            proficiency = 2
            armor = "Light and Medium"
            weapon = "Simple and Martial"
            shields = True
            saves = "Strength and Dexterity"
            toolz = "None"
            features = ["Favored Enemy", "Natural Explorer"]
            cantripz = []
            spellz = []
            pact = []
            domain = []
            sorOrig = []
            def skills():
                print(" 1. Animal Handling")
                print(" 2. Athletics")
                print(" 3. Insight")
                print(" 4. Investigation")
                print(" 5. Nature")
                print(" 6. Perception")
                print(" 7. Stealth")
                print(" 8. Survival")
                print(" You get 3 Skills to start.")
                i = 0
                while i < 3:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Animal Handling")
                    elif skillchoice == 2:
                        skill = skill.append("Athletics")
                    elif skillchoice == 3:
                        skill = skill.append("Insight")
                    elif skillchoice == 4:
                        skill = skill.append("Investigation")
                    elif skillchoice == 5:
                        skill = skill.append("Nature")
                    elif skillchoice == 6:
                        skill = skill.append("Perception")
                    elif skillchoice == 7:
                        skill = skill.append("Stealth")
                    elif skillchoice == 8:
                        skill = skill.append("Survial")
                    i += 1
                # skill1 = input(" Please choose your first skill by entering the name from above: ")
                # skill2 = input(" Please choose your second skill by entering the name from above: ")
                # skill3 = input(" Please choose your third skill by entering the name from above: ")
                return(skill)
            cskills = skills()
            domain = []
        elif classChoice == 9:
            playerClass = "Rogue"
            hitdie = 8
            proficiency = 2
            armor = "Light Armor"
            weapon = "Simple Weapons,Hand Crossbows,Longswords, Rapiers,Shortswords"
            shields = True
            saves = "Dexterity and Intelligence"
            toolz = "Thieves Tools"
            features = ["Expertise", "Sneak Attack","Thieves' Cant"]
            cantripz = []
            spellz = []
            pact = []
            domain = []
            sorOrig = []
            def skills():
                print(" 1. Acrobatics")
                print(" 2. Athletics")
                print(" 3. Deception")
                print(" 4. Insight")
                print(" 5. Intimidation")
                print(" 6. Investigation")
                print(" 7. Perception")
                print(" 8. Performance")
                print(" 9. Persuasion")
                print(" 10. Sleight of Hand")
                print(" 11. Stealth")
                print(" You get 4 Skills to start.")
                i = 0
                while i < 4:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Acrobatics")
                    elif skillchoice == 2:
                        skill = skill.append("Athletics")
                    elif skillchoice == 3:
                        skill = skill.append("Deception")
                    elif skillchoice == 4:
                        skill = skill.append("Insight")
                    elif skillchoice == 5:
                        skill = skill.append("Intimidation")
                    elif skillchoice == 6:
                        skill = skill.append("Investigation")
                    elif skillchoice == 7:
                        skill = skill.append("Perception")
                    elif skillchoice == 8:
                        skill = skill.append("Performance")
                    elif skillchoice == 9:
                        skill = skill.append("Persuasion")
                    elif skillchoice == 10:
                        skill = skill.append("Sleight of Hand")
                    elif skillchoice == 11:
                        skill = skill.append("Stealth")
                    i += 1
                # skill1 = input(" Please choose your first skill by entering the name from above: ")
                # skill2 = input(" Please choose your second skill by entering the name from above: ")
                # skill3 = input(" Please choose your third skill by entering the name from above: ")
                # skill4 = input(" Please choose your fourth skill by entering the name from above: ")
                return(skill)
            cskills = skills()
            domain = []
        elif classChoice == 10:
            playerClass = "Sorcerer"
            hitdie = 6
            proficiency = 2
            armor = "None"
            weapon = "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows"
            shields = True
            saves = "Constitution amd Charisma"
            toolz = "None"
            features = ["Spellcasting", "Sorcerous Origin"]
            domain = []
            pact = []
            def kantripz():
                cantrip = []
                print(" 1. Acid Splash")
                print(" 2. Blade Ward")
                print(" 3. Chill Touch")
                print(" 4. Dancing Lights")
                print(" 5. Fire Bolt")
                print(" 6. Friends")
                print(" 7. Light")
                print(" 8. Mage Hand")
                print(" 9. Mending")
                print(" 10. Message")
                print(" 11. Minor Illusion")
                print(" 12. Poison Spray")
                print(" 13. Prestidigitation")
                print(" 14. Ray of Frost")
                print(" 15. Shocking Grasp")
                print(" 16. True Strike")
                print(" You get 4 Cantrips to start.")
                i = 0
                while i < 4:
                    cantrip1txt = concat("  Please choose cantrip # ", str(i+1))
                    cantrip2txt = concat(cantrip1txt,": ")
                    cantripchoice = int(input(cantrip2txt))
                    if cantripchoice == 1:
                        cantrip.append("Acid Splash")
                    elif cantripchoice == 2:
                        cantrip.append("Blade Ward")
                    elif cantripchoice == 3:
                        cantrip.append("Chill Touch")
                    elif cantripchoice == 4:
                        cantrip.append("Dancing Lights")
                    elif cantripchoice == 5:
                        cantrip.append("Fire Bolt")
                    elif cantripchoice == 6:
                        cantrip.append("Friends")
                    elif cantripchoice == 7:
                        cantrip.append("Light")
                    elif cantripchoice == 8:
                        cantrip.append("Mage Hand")
                    elif cantripchoice == 9:
                        cantrip.append("Mending")
                    elif cantripchoice == 10:
                        cantrip.append("Message")
                    elif cantripchoice == 11:
                        cantrip.append("Minor Illusion")
                    elif cantripchoice == 12:
                        cantrip.append("Poison Spray")
                    elif cantripchoice == 13:
                        cantrip.append("Prestigitation")
                    elif cantripchoice == 14:
                        cantrip.append("Ray of Frost")
                    elif cantripchoice == 15:
                        cantrip.append("Shocking Grasp")
                    elif cantripchoice == 16:
                        cantrip.append("True Strike")
                    print(cantrip[i])
                    i += 1
                return(cantrip)
            cantripz = kantripz()

            def skills():
                skill = []
                print(" 1. Arcana")
                print(" 2. Deception")
                print(" 3. Insight")
                print(" 4. Intimidation")
                print(" 5. Persuasion")
                print(" 6. Religion")
                print(" You get 2 Skills.")
                i = 0
                while i < 2:
                    skillt1 = concat(" Please choose skill # ",str(i+1))
                    skillt2 = concat(skillt1," by entering the name from above: ")
                    skillchoice = int(input(skillt2))
                    if skillchoice == 1:
                        skill.insert(i,"Arcana")
                    elif skillchoice == 2:
                        skill.insert(i, "Deception")
                    elif skillchoice == 3:
                        skill.insert(i,"Insight")
                    elif skillchoice == 4:
                        skill.insert("Intimidation")
                    elif skillchoice == 5:
                        skill.insert("Persuasion")
                    elif skillchoice == 6:
                        skill.insert("Religion")
                    i += 1
                return(skill)
            cskills = skills()

            def sorcerous():
                print(" 1. Draconic Bloodline")
                print(" 2. Wild Magic")
                originCoice = int(input(" Please choose your Sorcerous Origin by entering the number from the list above: "))
                if originCoice == 2:
                    source ="Wild Magic"
                    sOrigin = ["Wild Magic Surge", "Tides of Chaos"]
                    return(source,sOrigin)
                else:
                    print(" 1. Black: Acid")
                    print(" 2. Copper: Acid")
                    print(" 3. Blue: Lightning")
                    print(" 4. Bronze: Lightning")
                    print(" 5. Brass: Fire")
                    print(" 6. Gold: Fire")
                    print(" 7. Red: Fire")
                    print(" 8. Green: Poison")
                    print(" 9. Silver: Cold")
                    print(" 10. White: Cold")
                    ancestry = int(input( " Please select a dragon ancestry: "))
                    if ancestry == 1:
                        dragon = "Black"
                        energy = "Acid"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 2:
                        dragon = "Copper"
                        energy = "Acid"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 3:
                        dragon = "Blue"
                        energy = "Lightning"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 4:
                        dragon = "Bronzer"
                        energy = "Lightning"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 5:
                        dragon = "Brass"
                        energy = "Fire"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 6:
                        dragon = "Gold"
                        energy = "Fire"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 7:
                        dragon = "Red"
                        energy = "Fire"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 8:
                        dragon = "Green"
                        energy = "Poison"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 9:
                        dragon = "Silver"
                        energy = "Cold"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)
                    elif ancestry == 10:
                        dragon = "White"
                        energy = "Cold"
                        source = "Draconic Bloodline"
                        sOrigin = [dragon,energy]
                        return(source,sOrigin)                
            sorOrig = sorcerous()

            def SpellSelection():
                print("  1. Burning Hands")
                print("  2. Charm Person")
                print("  3. Chromatic Orb")
                print("  4. Color Spray")
                print("  5. Comprehend Languages")
                print("  6. Detect Magic")
                print("  7. Disguise Self")
                print("  8. Expeditious Retreat")
                print("  9. False Life")
                print(" 10. Feather Fall")
                print(" 11. Fog Cloud")
                print(" 12. Jump")
                print(" 13. Mage Armor")
                print(" 14. Magic Missile")
                print(" 15. Ray of Sickness")
                print(" 16. Shield")
                print(" 17. Silent Image")
                print(" 18. Sleep")
                print(" 19. Thunderwave")
                print(" 20. Witch Bolt")
                print("Please select 2 spells")
                i = 2
                level1spells = []
                while i > 0:
                    spellconcat1 = (concat("Please select ",str(i)))
                    spellconcat2 = (concat(spellconcat1," more spells: "))
                    spellchoice = int(input(spellconcat2))
                    if spellchoice == 1:
                        level1spells.append("Burning Hands")
                    elif spellchoice == 2:
                        level1spells.append("Charm Person")
                    elif spellchoice == 3:
                        level1spells.append("Chromatic Orb")
                    elif spellchoice == 4:
                        level1spells.append("Color Spray")
                    elif spellchoice == 5:
                        level1spells.append("Comprehend Languages")
                    elif spellchoice == 6:
                        level1spells.append("Detect Magic")
                    elif spellchoice == 7:
                        level1spells.append("Disguise Self")
                    elif spellchoice == 8:
                        level1spells.append("Expeditios Retreat")
                    elif spellchoice == 9:
                        level1spells.append("False Life")
                    elif spellchoice == 10:
                        level1spells.append("Feather Fall")
                    elif spellchoice == 11:
                        level1spells.append("Fog Cloud")
                    elif spellchoice == 12:
                        level1spells.append("Jump")
                    elif spellchoice == 13:
                        level1spells.append("Mage Armor")
                    elif spellchoice == 14:
                        level1spells.append("Magic Missle")
                    elif spellchoice == 15:
                        level1spells.append("Ray of Sickness")
                    elif spellchoice == 16:
                        level1spells.append("Shield")
                    elif spellchoice == 17:
                        level1spells.append("Silent Image")
                    elif spellchoice == 18:
                        level1spells.append("Sleep")
                    elif spellchoice == 19:
                        level1spells.append("Thunderwave")
                    elif spellchoice == 20:
                        level1spells.append("Witch Bolt")
                    i -= 1
                return(level1spells)
            spellz = SpellSelection()
        elif classChoice == 11:
            playerClass = "Warlock"
            hitdie = 8
            proficiency = 2
            armor = "Light Armor"
            weapon = "Simple Weapons"
            shields = False
            saves = "Wisdom and Charisma"
            toolz = "None"
            features = ["Otherworldly Patron", "Pact Magic"]
            sorOrig = []
            domain = []
            def patron():
                print(" 1. Archfey")
                print(" 2. Fiend")
                print(" 3. Great Old One")
                patronchoice = int(input(" Please select a patron: "))
                if patronchoice == 1:
                    print(" 1. Jack Frost")
                    print(" 2. Summet Queen")
                    print(" 3. Winter Queen")
                    print(" 4. King Oberon")
                    print(" 5. Green Lord")
                    print(" 6. Hyrsam")
                    print(" 7. Robin Goodfellow")
                    print(" 8. Name Your own:")
                    choice = int(input("Please choose a patron"))
                    if choice == 1:
                        pact = "Jack Frost"
                        return(pact)
                    elif choice == 2:
                        pact = "Summer Queen"
                        return(pact)
                    elif choice == 3:
                        pact = "Winter Queen"
                        return(pact)
                    elif choice == 4:
                        pact = "King Oberon"
                        return(pact)
                    elif choice == 5:
                        pact = "Jack Frost"
                        return(pact)
                    elif choice == 6:
                        pact = "Summer Queen"
                        return(pact)
                    elif choice == 7:
                        pact = "Winter Queen"
                        return(pact)
                    elif choice == 8:
                        pact = input("Please name an Archfey as your patron: ")
                        return(pact)
                elif patronchoice == 2:
                    pact = int(input(" Please name a fiend as a patron: "))
                    return(pact)
                elif patronchoice == 3:
                    pact = int(input(" Please name an otherworldly being (nondiety) as a patron: "))
                    return(pact)
                return(pact)
            pact = patron()
            def kantripz():
                cantrip = []
                print(" 1. Blade Ward")
                print(" 2. Chill Touch")
                print(" 3. Eldrich Blast")
                print(" 4. Friends")
                print(" 5. Mage Hand")
                print(" 6. Minor Illusion")
                print(" 7. Poison Spray")
                print(" 8. Prestidigitation")
                print(" 9. True Strike")
                print(" You get 2 Cantrips to start.")
                i = 0
                while i < 2:
                    cantrip1txt = concat("  Please choose cantrip # ", str(i+1))
                    cantrip2txt = concat(cantrip1txt,": ")
                    cantripchoice = int(input(cantrip2txt))
                    if cantripchoice == 1:
                        cantrip.append("Blade Ward")
                    elif cantripchoice == 2:
                        cantrip.append("Chill Touch")
                    elif cantripchoice == 3:
                        cantrip.append("Eldrich Blast")
                    elif cantripchoice == 4:
                        cantrip.append("Friends")
                    elif cantripchoice == 5:
                        cantrip.append("Mage Hand")
                    elif cantripchoice == 6:
                        cantrip.append("Minor Illusion")
                    elif cantripchoice == 7:
                        cantrip.append("Poison Spray")
                    elif cantripchoice == 8:
                        cantrip.append("Prestigitation")
                    elif cantripchoice == 9:
                        cantrip.append("True Strike")
                    print(cantrip[i])
                    i += 1
                return(cantrip)
            cantripz = kantripz()
            def skills():
                print(" 1. Arcana")
                print(" 2. Deception")
                print(" 3. History")
                print(" 4. Intimidation")
                print(" 5. Investigation")
                print(" 6. Nature")
                print(" 7. Religion")
                print(" You get 2 Skills.")
                i = 0
                while i < 2:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the number from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Arcana")
                    elif skillchoice == 2:
                        skill = skill.append("Deception")
                    elif skillchoice == 3:
                        skill = skill.append("History")
                    elif skillchoice == 4:
                        skill = skill.append("Intimidation")
                    elif skillchoice == 5:
                        skill = skill.append("Investigation")
                    elif skillchoice == 6:
                        skill = skill.append("Nature")
                    elif skillchoice == 7:
                        skill = skill.append("Religion")
                    i += 1
                return(skill)
            cskills = skills()
            def SpellSelection():
                print("  1. Armor of Agathys")
                print("  2. Arms of Hadar")
                print("  3. Charm Person")
                print("  4. Comprehend Languages")
                print("  5. Expeditious Retreat")
                print("  6. Hellish Rebuke")
                print("  7. Hex")
                print("  8. Illusory Script")
                print("  9. Protection from Evil and Good")
                print(" 10. Witch Bolt")
                i = 2
                level1spells = []
                while i > 0:
                    spellconcat1 = (concat("Please select ",str(i)))
                    spellconcat2 = (concat(spellconcat1," more spells: "))
                    spellchoice = int(input(spellconcat2))
                    if spellchoice == 1:
                        level1spells.append("Armor of Agathys")
                    elif spellchoice == 2:
                        level1spells.append("Arms of Hadar")
                    elif spellchoice == 3:
                        level1spells.append("Charm Person")
                    elif spellchoice == 4:
                        level1spells.append("Comprehend Languages")
                    elif spellchoice == 5:
                        level1spells.append("Expeditious Retreat")
                    elif spellchoice == 6:
                        level1spells.append("Hellish Rebuke")
                    elif spellchoice == 7:
                        level1spells.append("Hex")
                    elif spellchoice == 8:
                        level1spells.append("Illusory Script")
                    elif spellchoice == 9:
                        level1spells.append("Protection from Evil and Good")
                    elif spellchoice == 10:
                        level1spells.append("Witch Bolt")
                    elif spellchoice == 19:
                        level1spells.append("Tasha’s Hideous Laughter")
                    elif spellchoice == 20:
                        level1spells.append("Thunderwave")
                    elif spellchoice == 21:
                        level1spells.append("Unseen Servant")
                    i -= 1
                return(level1spells)
            spellz = SpellSelection()
        elif classChoice == 12:
            playerClass = "Wizard"
            hitdie = 6
            proficiency = 2
            armor = "None"
            weapon = "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows"
            shields = False
            saves = "Intelligence and Wisdom"
            features = ["Spell Casting","Arcane Recovery"]
            spellz = []
            pact = []
            cskills = []
            domain = []
            toolz = "None"
            sorOrig = []
        
            def kantripz():
                cantrip = []
                print(" 1. Acid Splash")
                print(" 2. Blade Ward")
                print(" 3. Chill Touch")
                print(" 4. Dancing Lights")
                print(" 5. Fire Bolt")
                print(" 6. Friends")
                print(" 7. Light")
                print(" 8. Mage Hand")
                print(" 9. Mending")
                print(" 10. Message")
                print(" 11. Minor Illusion")
                print(" 12. Poison Spray")
                print(" 13. Prestidigitation")
                print(" 14. Ray of Frost")
                print(" 15. Shocking Grasp")
                print(" 16. True Strike")
                print(" You get 2 Cantrips to start.")
                i = 0
                while i < 3:
                    cantrip1txt = concat("  Please choose cantrip # ", str(i+1))
                    cantrip2txt = concat(cantrip1txt,": ")
                    cantripchoice = int(input(cantrip2txt))
                    if cantripchoice == 1:
                        cantrip.append("Acid Splash")
                    elif cantripchoice == 2:
                        cantrip.append("Blade Ward")
                    elif cantripchoice == 3:
                        cantrip.append("Chill Touch")
                    elif cantripchoice == 4:
                        cantrip.append("Dancing Lights")
                    elif cantripchoice == 5:
                        cantrip.append("Fire Bolt")
                    elif cantripchoice == 6:
                        cantrip.append("Friends")
                    elif cantripchoice == 7:
                        cantrip.append("Light")
                    elif cantripchoice == 8:
                        cantrip.append("Mage Hand")
                    elif cantripchoice == 9:
                        cantrip.append("Mending")
                    elif cantripchoice == 10:
                        cantrip.append("Message")
                    elif cantripchoice == 11:
                        cantrip.append("Minor Illusion")
                    elif cantripchoice == 12:
                        cantrip.append("Poison Spray")
                    elif cantripchoice == 13:
                        cantrip.append("Prestidigitation")
                    elif cantripchoice == 14:
                        cantrip.append("Ray of Frost")
                    elif cantripchoice == 15:
                        cantrip.append("Shocking Grasp")
                    elif cantripchoice == 16:
                        cantrip.append("True Strike")
                    print(cantrip[i])
                    i += 1
                return(cantrip)
            cantripz = kantripz()
            
            def skills():
                print(" 1. Arcana")
                print(" 2. History")
                print(" 3. Insight")
                print(" 4. Investigation")
                print(" 5. Medicine")
                print(" 6. Religion")
                print(" You get 2 Skills.")
                i = 0
                while i < 2:
                    skill = []
                    skillt1 = concat(" Please choose skill ",str(i+1))
                    skillt2 = concat(skillt1," by entering the number from above: ")
                    skillchoice = input(skillt2)
                    if skillchoice == 1:
                        skill = skill.append("Arcana")
                    elif skillchoice == 2:
                        skill = skill.append("History")
                    elif skillchoice == 3:
                        skill = skill.append("Insight")
                    elif skillchoice == 4:
                        skill = skill.append("Investigation")
                    elif skillchoice == 5:
                        skill = skill.append("Medicine")
                    elif skillchoice == 6:
                        skill = skill.append("Religion")
                    i += 1
                return(skill)
            cskills = skills()

            def SpellSelection():
                print(" 1. Alarm")
                print(" 2. Burning Hands")
                print(" 3. Charm Person")
                print(" 4. Chromatic Orb")
                print(" 5. Color Spray")
                print(" 6. Comprehend Languages")
                print(" 7. Detect Magic")
                print(" 8. Disguise Self")
                print(" 9. Expeditious Retreat")
                print(" 10. False Life")
                print(" 11. Feather Fall")
                print(" 12. Find Familiar")
                print(" 13. Fog Cloud")
                print(" 14. Grease")
                print(" 15. Identify")
                print(" 16. Illusory Script")
                print(" 17. Jump")
                print(" 18. Longstrider")
                print(" 19. Mage Armor")
                print(" 20. Magic Missile")
                print(" 21. Protection from Evil and Good")
                print(" 22. Ray of Sickness")
                print(" 23. Shield")
                print(" 24. Silent Image")
                print(" 25. Sleep")
                print(" 26. Tasha’s Hideous Laughter")
                print(" 27. Tenser’s Floating Disk")
                print(" 28. Thunderwave")
                print(" 29. Unseen Servant")
                print(" 30. Witch Bolt")
                i = 6
                level1spells = []
                while i > 0:
                    spellconcat1 = (concat("Please select ",str(i)))
                    spellconcat2 = (concat(spellconcat1," more spells: "))
                    spellchoice = int(input(spellconcat2))
                    if spellchoice == 1:
                        level1spells.append("Alarm")
                    elif spellchoice == 2:
                        level1spells.append("Burning Hands")
                    elif spellchoice == 3:
                        level1spells.append("Charm Person")
                    elif spellchoice == 4:
                        level1spells.append("Chromatic Orb")
                    elif spellchoice == 5:
                        level1spells.append("Color Spray")
                    elif spellchoice == 6:
                        level1spells.append("Comprehend Languages")
                    elif spellchoice == 7:
                        level1spells.append("Detect Magic")
                    elif spellchoice == 8:
                        level1spells.append("Disguise Self")
                    elif spellchoice == 9:
                        level1spells.append("Expeditious Retreat")
                    elif spellchoice == 10:
                        level1spells.append("False Life")
                    elif spellchoice == 11:
                        level1spells.append("Feather Fall")
                    elif spellchoice == 12:
                        level1spells.append("Find Familiar")
                    elif spellchoice == 13:
                        level1spells.append("Fog Cloud")
                    elif spellchoice == 14:
                        level1spells.append("Grease")
                    elif spellchoice == 15:
                        level1spells.append("Identify")
                    elif spellchoice == 16:
                        level1spells.append("Illusory Script")
                    elif spellchoice == 17:
                        level1spells.append("Jump")
                    elif spellchoice == 18:
                        level1spells.append("Long Strider")
                    elif spellchoice == 19:
                        level1spells.append("Mage Armor")
                    elif spellchoice == 20:
                        level1spells.append("Magic Missle")
                    if spellchoice == 21:
                        level1spells.append("Protection from Evil and Good")
                    elif spellchoice == 22:
                        level1spells.append("Ray of Sickness")
                    elif spellchoice == 23:
                        level1spells.append("Shield")
                    elif spellchoice == 24:
                        level1spells.append("Silent Image")
                    elif spellchoice == 25:
                        level1spells.append("Sleep")
                    elif spellchoice == 26:
                        level1spells.append("Tasha's Hideous Laughter")
                    elif spellchoice == 27:
                        level1spells.append("Tenser's Floating Disk")
                    elif spellchoice == 28:
                        level1spells.append("Thunderwave")
                    elif spellchoice == 29:
                        level1spells.append("Unseen Servant")
                    elif spellchoice == 30:
                        level1spells.append("Witch Bolt")
                    i -= 1
                return(level1spells)
            spellz = SpellSelection()
        # elif classChoice == 13:
        #     playerClass = "Artificer"
        #     hitdie = 6
        #     proficiency = 2
        #     armor = "Light and Medium"
        #     weapon = "Simple and Martial"
        #     shields = True
        #     saves = "Strength and Constitution"
        #     spellz = []
        #     domain = []
        #     sorOrig = []
        return(playerClass,hitdie,proficiency,armor,weapon,shields,saves,features,cskills,toolz,cantripz,domain,spellz,sorOrig, pact)
    
    race = pRace()
    PlayClass = Pclass()
    return(pname,gender,race,PlayClass,strength,strmod,dexterity,dexmod,constitution,conmod,intelligence,intmod,wisdom,wismod,charisma,chamod)
player = playerStats()
pname = player[0]
race = player[2][0]
pclass = player[3][0]
strength += player[2][1]
strmod = math.floor((strength - 10)/2)
dexterity += player[2][2]
dexmod = math.floor((dexterity - 10)/2)
constitution += player[2][3]
conmod = math.floor((constitution - 10)/2)
intelligence += player[2][4]
intmod = math.floor((intelligence - 10)/2)
wisdom += player[2][5]
wismod = math.floor((wisdom - 10)/2)
charisma += player[2][6]
chamod = math.floor((charisma - 10)/2)
hp = player[3][1] + conmod
proficiency = player[3][2]
armor = player[3][3]
weapons = player[3][4]
shields = player[3][5]
saves = player[3][6]
features = player[3][7]
skills = player[3][8]
tools = player[3][9]
cantrips = player[3][10]
domain = player[3][11]
spells = player[3][12]
origin = player[3][13]
pact = player[3][14]
traits = player[2][7]
print("There are ",len(traits)," traits")
filename = concat(pname,".txt")
#######################################
datafile = open(filename,"tw")
datafile.write("Name: ")
datafile.write(pname)
datafile.write("\nGender: ")
datafile.write(player[1])
datafile.write("\nRace: ")
datafile.write(race)
datafile.write("\nClass: ")
datafile.write(pclass)
datafile.write("\nStrength: ")
datafile.write(str(strength))
datafile.write(" ")
datafile.write(str(strmod))
datafile.write("\nDexterity: ")
datafile.write(str(dexterity))
datafile.write(" ")
datafile.write(str(dexmod))
datafile.write("\nConstitution: ")
datafile.write(str(constitution))
datafile.write(" ")
datafile.write(str(conmod))
datafile.write("\nIntelligence: ")
datafile.write(str(intelligence))
datafile.write(" ")
datafile.write(str(intmod))
datafile.write("\nWisdom: ")
datafile.write(str(wisdom))
datafile.write(" ")
datafile.write(str(wismod))
datafile.write("\nCharisma: ")
datafile.write(str(charisma))
datafile.write(" ")
datafile.write(str(chamod))
datafile.write("\n\n########################################################################################\n\n")
datafile.write("Racial Traits\n")
i = 0
while i < len(traits):
    traitstxt1 = concat("\nRacial Trait",str(i+1))
    traitstxt2 = concat(traitstxt1,": ")
    datafile.write(traitstxt2)
    datafile.write(traits[i])
    i += 1
datafile.write("\n\n########################################################################################\n")
datafile.write("\nHP: ")
datafile.write(str(hp))
datafile.write("\nProficieny: +")
datafile.write(str(proficiency))
datafile.write("\nArmor: ")
datafile.write(armor)
datafile.write("\nWeapons: ")
datafile.write(weapons)
datafile.write("\nShields: ")
datafile.write(str(shields))
datafile.write("\nSaves: ")
datafile.write(saves)

i = 0
while i < len(features):
    featurestxt1 = concat("\nFeature ",str(i+1))
    featurestxt2 = concat(featurestxt1,": ")
    datafile.write(featurestxt2)
    datafile.write(features[i])
    i += 1

datafile.write("\nTools: ")
datafile.write(tools)

i = 0
while i < len(skills):
    skilltxt = concat("\nSkill",str(i+1))
    Skill = concat(skilltxt,": ")
    datafile.write(Skill)
    datafile.write(skills[i])
    i+= 1

i = 0
while i < len(cantrips):
    cantriptxt = concat("\nCantrip",str(i+1))
    Cantrip = concat(cantriptxt,": ")
    datafile.write(Cantrip)
    datafile.write(cantrips[i])
    i+= 1

if len(domain) > 0:
    i = 0
    while i < len(domain):
        Domaintxt1 = concat("\nDivine Domain",str(i+1))
        Domaintxt2 = concat(Domaintxt1,": ")
        datafile.write(Domaintxt2)
        datafile.write(domain[i])
        datafile.write("\nDomain Spell1: ")
        datafile.write(domain[i])
        i += 1

if len(spells) > 0:
    j = 0
    while j < len(spells):
        SpellzConcat1 = concat("\nSpell ",str(j+1))
        SpellzConcat2 = concat(SpellzConcat1,": ")
        datafile.write(SpellzConcat2)
        datafile.write(spells[j])
        j += 1

if len(pact) > 0:
    datafile.write("\nParton: ")
    datafile.write(pact)

elif pclass == "Sorcerer":
    datafile.write("\nSorcerous Origin: ")
    datafile.write(origin[0])
    datafile.write("\nSorcerous Ancestry: ")
    i = 0
    while i < len(origin[1]):
        datafile.write(origin[1][i])
        datafile.write(": ")
        i += 1
    j = 0
    while j < len(spells): 
        SpellzConcat1 = concat("\nSepll ",str(j+1))
        SpellzConcat2 = concat(SpellzConcat1,": ")
        datafile.write(SpellzConcat2)
        datafile.write(spells[j])
        j += 1
    datafile.close

else:
    datafile.close