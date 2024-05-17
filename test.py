import json
import os
## Create Class for creating new dictionaries here

with open("characterinfo.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here


Character_Name = []
Faction = []
HP = 0
ATK = 0
ENERGY = 0

class main_character():
  def __init__(self, Role, Name, HP, ATK, ENERGY):
    self.Role = Role
    self.Name = Name
    self.HP = HP
    self.ATK = ATK
    self.ENERGY = ENERGY

class roles2(main_character):
  def Warrior(self, HP, ATK, ENERGY):
    self.HP = HP
    self.ATK = ATK
    self.ENERGY = ENERGY
    self.HP = 120
    self.ATK = 20
    self.ENERGY = 100
    data.append(main_character.__dict__)
  def Archer(self, HP, ATK, ENERGY):
    self.HP = HP
    self.ATK = ATK
    self.ENERGY = ENERGY
    self.HP = 100
    self.ATK = 15
    self.ENERGY = 150
    data.append(main_character.__dict__)
  def Mage(self, HP, ATK, ENERGY):
    self.HP = HP
    self.ATK = ATK
    self.ENERGY = ENERGY
    self.HP = 80
    self.ATK = 20
    self.ENERGY = 200
    data.append(main_character.__dict__)
    

class CharacterFinder():
 def Search_CharacterName(data):
  while input:
   Z = input("Input Character Name: ")
   for main_character in data:
    if Z in (main_character['Name']) :
     print("Name:",main_character['Name'])
     print("Role:",main_character['Role'])
     print("HP:",main_character['HP'])
     print("ATK:",main_character['ATK'])
     print("ENERGY:",main_character['ENERGY'])
     print("Confirm to load",Z,"? (Y/N) ")
     break
   Con = input("")
   if Con == 'Y':
    print("Loading save...")
    break
   elif Con == 'N':
    Z = ''

print("Welcome to Derek's Brainrot Simulator")
Begin = input("Type 'START' to start a new game and 'EXIT' to exit game ")
if Begin == 'START':
    New_Save = input("Start a new save file? (Y/N) ")
    if New_Save == 'Y':
     while input:
      Name = input("Input Charcter Name: ")
      print("Confirm to name your character", Name, "? (Y/N) ")
      Confirm = input("")
      if Confirm == 'Y':
       Character_Name.append(Name)
       print(Character_Name)
       print("Warrior Stats: 120 HP, 20 ATK, 100 MAX ENERGY")
       print("Mage Stats: 80 HP, 10 ATK, 200 MAX ENERGY")
       print("Archer Stats: 100 HP, 15 ATK, 150 MAX ENERGY")
       print("Choose", Name,"'s role: ")
       Role = input("Warrior, Mage, or Archer? ")
       Faction.clear
       Faction.append(Role)
       if Role == 'Warrior':
        roles2.Warrior(HP, ATK, ENERGY)
        break
       elif Role == 'Mage':
        roles2.Mage(HP, ATK, ENERGY)
        break
       elif Role == 'Archer':
        roles2.Archer(HP, ATK, ENERGY)
        break
      if Confirm == 'N':
       Name = ' '
    elif New_Save == 'N':
       F = input("Open A Previous Save? ")
       if F == 'Y':
        CharacterFinder.Search_CharacterName(data)
       else:
        print("Stop Trolling and Get a Life")
if Begin == 'EXIT':
 print("Womp Womp")
 print("Exiting Game")

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("characterinfo.json")
os.rename(new_file, "characterinfo.json")