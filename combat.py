import json
import os

## Create Class for creating new dictionaries here
with open("characterinfo.json", "r") as f:


  
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
class Games():
    def __init__(self, Name, HP, ATK, ENERGY, Role):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.ENERGY = ENERGY
        self.Role = Role
    ##Call classes in here

while True:
    Name = input("Enter Character Name: ")
    R = ---
    G = input("Enter Game Genre: ")
    games = Games(N,R,G)
    data.append(games.__dict__)
    new_game = input("Do you want to enter a new game? Y/N ")
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
os.remove("data.json")
os.rename(new_file, "data.json")