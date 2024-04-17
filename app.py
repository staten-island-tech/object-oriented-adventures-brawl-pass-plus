import json
import os

## Create Class for creating new dictionaries here
with open("enemyinfo.json", "r") as f:


  
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
class Enemies():
    def __init__(self, name, atk, hp, skill):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.skill = skill
    ##Call classes in here

while True:
    N = input("Enter Enemy Name: ")
    A = int(input("Enter Enemy ATK: "))
    H = int(input("Enter Enemy HP: "))
    S = input("Enter Enemy Skill: ")
    enemies = Enemies(N,A,H,S)
    data.append(enemies.__dict__)
    new_enemy = input("Do you want to enter a new enemy? Y/N ")
    if new_enemy.upper()== "N":
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
os.remove("data.json")
os.rename(new_file, "data.json")