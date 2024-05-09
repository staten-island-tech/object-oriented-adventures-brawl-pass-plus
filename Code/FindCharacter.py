import json 
## Create Class for creating new dictionaries here
with open("characterinfo.json", "r") as f:
# Serialize the updated Python list to a JSON string
 main_characters = open("characterinfo.json", encoding="utf8")
 data = json.load(main_characters)
# create variable "data" that represents the enitre pokedex list

class CharacterFinder():
 def Search_CharacterName(data):
  Z = input("Input Character Name: ")
  for main_character in data:
   if Z in main_character['Name'] :
    print("Name:",main_character['Name'])
    print("Role:",main_character['Role'])
    print("HP:",main_character['HP'])
    print("ATK:",main_character['ATK'])
    print("ENERGY:",main_character['ENERGY'])
   else:
    print("No character data found for", Z)

CharacterFinder.Search_CharacterName(data)