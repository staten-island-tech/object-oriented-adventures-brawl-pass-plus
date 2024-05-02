Character_Name = []
Faction = []
HP = 0
ATK = 0
ENERGY = 0

print("Welcome to Derek's Brainrot Simulator")
Begin = input("Type 'START' to start a new game and 'EXIT' to exit game ")
if Begin == 'START':
    New_Save = input("Start a new save file? (Y/N) ")
    if New_Save == 'Y':
     Character_Name.clear
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
         HP = 120
         ATK = 20
         ENERGY = 100
         print(Name,"is a", Role)
         print("HP:", HP, "ATK:", ATK, "ENERGY:", ENERGY)
         break
       elif Role == 'Mage':
         HP = 80
         ATK = 10
         ENERGY = 200
         print(Name,"is a", Role)
         print("HP:", HP, "ATK:", ATK, "ENERGY:", ENERGY)
         break
       elif Role == 'Archer':
         HP = 100
         ATK = 15
         ENERGY = 150
         print(Name,"is an", Role)
         print("HP:", HP, "ATK:", ATK, "ENERGY:", ENERGY)
         break
      if Confirm == 'N':
       Name = ' '
    elif New_Save == 'N':
      F = input("Open A Previous Save? ")
      if F == 'Y':
        print("Work in Progress")
      if F == 'N':
        print("Stop Trolling and Get a Life")