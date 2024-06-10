import json
enemies = open("enemyinfo.json", encoding="utf8")
character = open("characterinfo.json", encoding="utf8")
data = json.load(enemies)
cdata = json.load(character)

Character = []
All = []
Enemy = []
Enemy_HP = []
Enemy_ATK = []
Character_Energy = []
Character_DefaultEnergy = []
Character_ATK = []
Character_DefaultATK = []
Character_HP = []
Character_DefaultHP = []
Input = []
Input2 = []
Input3 = []
Status = []
Character_Status = []
availableskillpoints = []
Character_Role = []

class combat():
 def Search_CharacterName(cdata):
    Z = input("Input Character Name: ")
    for main_character in cdata:
     if Z in main_character['Name'] :
      Character.append(main_character['Name'])
      Character_Energy.append(main_character['ENERGY'])
      Character_DefaultEnergy.append(main_character['ENERGY'])
      Character_ATK.append(main_character['ATK'])
      Character_DefaultATK.append(main_character['ATK'])
      Character_HP.append(main_character['HP'])
      Character_DefaultHP.append(main_character['HP'])
      availableskillpoints.append(main_character['Skillpoints'])
      Character_Role.append(main_character['Role'])
 def Available_Enemies(data):
  for basic_enemies in data:
   X = int(''.join(map(str, Character_HP)))
   if X > basic_enemies['HP']:
    Enemy.append(basic_enemies['Name'])

combat.Search_CharacterName(cdata)
combat.Available_Enemies(data)
print("These are the enemies you can fight", Enemy)


  
