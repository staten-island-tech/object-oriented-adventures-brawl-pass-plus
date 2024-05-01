import json
import os

<<<<<<< HEAD
print("Welcome to Derek's Brainrot Simulator")
Begin = input("Type 'START' to start a new game and 'EXIT' to exit game ")
if Begin == 'START':
    New_Save = input("Start a new save file? (Y/N) ")
    if New_Save == 'Y':
     Name = input("Input Charcter Name: ")
     Confirm = input("Confirm to name your character",Name,"? (Y/N) ")
     if Confirm == "Y":
      Character_Name.append(Name)
     if Confirm == "N":
      Name == ' '
=======
with open("characterinfo.json", "r") as f:

    data = json.load(f)
class Faction():
    def __init__ (self,hp,atk,energy):
        self.hp = hp
        self.atk = atk
        self.energy = energy

class Warrior(Faction):
    def stats(self):
        self.name = "Warrior"
        self.atk = 5
        self.hp = 50
        self.energy = 100

class Mage(Faction):
    def stats(self):
        self.name = "Mage"
        self.atk = 5
        self.hp = 50
        self.energy = 200

class Archer(Faction):
    def stats(self):
        self.name = "Slime"
        self.atk = 5
        self.hp = 50
        self.energy = 150
class Character():
   def __init__ (self, username, hp, atk, energy):
      self.username = username
      self.hp = hp
      self.atk = atk
      self.energy = energy

while True:
    print("Welcome to Derek's Brainrot Simulator")
    X = input("Type 'START' to start a new game and 'EXIT' to exit game ")
    if X == 'START':
        Y = input("Start a new save file? (Y/N) ")
        if Y == 'Y':
        U = input("Input Charcter Name: ")
        C = input("Choose your faction: " )
        Character.stats(data)
        print("Confirm to name your character",U,"?")

        data.append(Character.__dict__)
        break


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(data)


    f.write(json_string)


os.remove("data.json")
os.rename(new_file, "data.json")
>>>>>>> fcc965646d624fada9f66052b61ab640efec0878
