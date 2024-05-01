Character_Name = []

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