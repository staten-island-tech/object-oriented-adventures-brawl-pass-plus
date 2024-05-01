Character_Name = []

print("Welcome to Derek's Brainrot Simulator")
X = input("Type 'START' to start a new game and 'EXIT' to exit game ")
if X == 'START':
    Y = input("Start a new save file? (Y/N) ")
    if Y == 'Y':
     Name = input("Input Charcter Name: ")
     print("Confirm to name your character",Name,"?")
     Character_Name.append(Name)