import json
import os

## Create Class for creating new dictionaries here
with open("enemyinfo.json", "r") as f:


  
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
class Games():
    def __init__(self, name, attack, hp, skill):
        self.name = name
        self.attack = attack
        self.hp = hp  
        self.skill = skill
    ##Call classes in here

while True:
    N = input("Enter Enemy Name: ")
    R = int(input("Enter Enemy Attack: "))
    G = int(input("Enter Enemy Hp: "))
    S = input("Enter Enemy Skill: ")
    games = Games(N,R,G,S)
    data.append(games.__dict__)
    new_game = input("Do you want to enter a new enemy info? Y/N ")
    if new_game.upper()== "N":
        break






#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("enemyinfo.json")
os.rename(new_file, "enemyinfo.json")