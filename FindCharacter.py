import json 
## Create Class for creating new dictionaries here
with open("characterinfo.json", "r") as f:
# Serialize the updated Python list to a JSON string
 main_characters = open("characterinfo.json", encoding="utf8")
 data = json.load(main_characters)
# create variable "data" that represents the enitre pokedex list

def Search_CharacterName(data):
  Z = input("Input Character Name: ")
  for main_character in data:
   if Z in main_character['Name'] :
    print(print(main_character['Name'], main_character['Role'], main_character['HP'], main_character['ATK'], main_character['ENERGY']))

