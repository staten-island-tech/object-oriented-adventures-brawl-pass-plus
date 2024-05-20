import json
enemies = open("enemyinfo.json", encoding="utf8")
character = open("characterinfo.json", encoding="utf8")
data = json.load(enemies)
cdata = json.load(character)


Character_Energy = ''

Z = input("Input Character Name: ")
for main_character in cdata:
     if Z in main_character['Name'] :
      Character_Energy = (main_character['ENERGY'])
      print(Character_Energy)