import json
enemies = open("enemyinfo.json", encoding="utf8")
character = open("characterinfo.json", encoding="utf8")
data = json.load(enemies)
cdata = json.load(character)

Character = []
Enemy = []
Enemy_HP = []
Character_Energy = []
Character_ATK = []
Character_HP = []
Input = []
Input2 = []

class combat():
 def Search_CharacterName(cdata):
    Z = input("Input Character Name: ")
    for main_character in cdata:
     if Z in main_character['Name'] :
      Character.append(main_character['Name'])
      Character_Energy.append(main_character['ENERGY'])
      Character_ATK.append(main_character['ATK'])
      Character_HP.append(main_character['HP'])
 def Search_EnemyName(data):
  E = input("Input Enemy Name: ")
  for basic_enemies in data:
   if E in basic_enemies['Name'] :
    Enemy.append(basic_enemies['Name'])
    Enemy_HP.append(basic_enemies['HP'])
    print("Welcome to the tutorial", Character)
 def attack():
    E = ''.join(Enemy)
    Z = ''.join(Character)
    for basic_enemies in data:
        for main_character in cdata:
            if Z in main_character['Name']:
                if E in basic_enemies['Name']:
                    x = (basic_enemies["HP"])
                    y = (main_character["ATK"])
                    finalhp = x - y
                    Enemy_HP.append(finalhp)
                    print ("The",Enemy,"has",finalhp,"HP remaining")
 def enhance_attack():
    X = input("how much energy do you want to use? ")
    Y = int(X)
    Input.append(Y)
    if Input > Character_Energy:
        print ("you don't have enough energy!")
    else:
        Final_ATK = (Input + Character_ATK)
        Z = sum(Final_ATK)
        Character_ATK.clear
        Character_ATK.append(Z)
        print("Your new attack is:", Z)
        W = (Character_Energy - Input)
        Character_Energy.clear
        Character_Energy.append(W)
 def heal():
    X = input("how much energy do you want to use? ")
    Y = int(X)
    Input2.append(Y)
    W = Character_Energy - Input2
    Character_Energy.clear
    Character_Energy.append(W)
    if Input2 > Character_Energy:
        print ("you don't have enough energy!")
    else:
        Final_HP = (Input2 + Character_HP)
        Z = sum(Final_HP)
        print("Your new HP is:", Z)
        Character_HP.clear
        Character_HP.append(Z)
 def continue_attack():
    E = ''.join(Enemy)
    Z = ''.join(Character)
    for basic_enemies in data:
        for main_character in cdata:
            if Z in main_character['Name']:
                if E in basic_enemies['Name']:
                    x = int(Enemy_HP)
                    y = (main_character["ATK"])
                    finalhp = (x - y)
                    Enemy_HP.clear
                    Enemy_HP.append(finalhp)
                    print ("The",Enemy,"has",Enemy_HP,"HP remaining")
 """ def continue_enhance():
    X = input("how much energy do you want to use? ")
    Y = int(X)
    Input.clear
    Input.append(Y)
    if Input > Character_Energy:
        print ("you don't have enough energy!")
    else:
        Final_ATK = (Input + Character_NewATK)
        Z = sum(Final_ATK)
        Character_NewATK.clear
        Character_NewATK.append(Z)
        print("Your new attack is:", Z)
        W = (Character_Energy + Input)
        Character_NewEnergy.append(W)
 def continue_heal():
    X = input("how much energy do you want to use? ")
    Y = int(X)
    Input2.clear
    Input2.append(Y)
    W = Character_NewEnergy - Input2
    Character_NewEnergy.clear
    Character_NewEnergy.append(W)
    if Input2 > Character_Energy:
        print ("you don't have enough energy!")
    else:
        Final_HP = (Input2 + Character_HP)
        Z = sum(Final_HP)
        print("Your new HP is:", Z)
        Character_NewHP.append(Z) """
 def retreat():
    print ("retreating from battle (imagine being a scaredy cat)")
 def exit_game():
    print ("exiting game...")
 

""" print("1 = [attack], 2 = [enhance attack], 3 = [heal], 4 = [retreat], 5 = [exit game]")
X = input()
if X == '1':
    combat.attack()
elif X == '2':
    combat.enhance_attack()
elif X == '3':
    combat.heal()
elif X == '4':
    combat.retreat()
elif X == '5':
    combat.exit_game() """

combat.Search_CharacterName(cdata)
combat.Search_EnemyName(data)
combat.attack()
while input:
 Z = input("Continue Attack? ")
 if Z == "Y":
  combat.continue_attack()
  Z = ''
 else:
  print("Dead")
   