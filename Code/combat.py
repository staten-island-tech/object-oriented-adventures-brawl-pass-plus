import json
enemies = open("enemyinfo.json", encoding="utf8")
character = open("characterinfo.json", encoding="utf8")
data = json.load(enemies)
cdata = json.load(character)


Character = []
All_Enemies = []
Enemy = []
Enemy_HP = []
Enemy_ATK = []
Character_Energy = []
Character_DefaultEnergy = []
Character_ATK = []
Character_DefaultATK = []
Character_HP = []
Character_DefaultHP = []
Input = []
Input2 = []
Input3 = []
Status = []
Character_Status = []
availableskillpoints = []
Character_Role = []
Can_Fight = []


class main_character():
    def __init__(self, Name, Role, HP, ATK, ENERGY, Skillpoints):
        self.Name = Name
        self.Role = Role
        self.HP = HP
        self.ATK = ATK
        self.ENERGY = ENERGY
        self.Skillpoints = Skillpoints


class combat():
 def Search_CharacterName(cdata):
    Z = input("Confirm Character Name: ")
    for main_character in cdata:
     if Z in main_character['Name'] :
      Character.append(main_character['Name'])
      Character_Energy.append(main_character['ENERGY'])
      Character_DefaultEnergy.append(main_character['ENERGY'])
      Character_ATK.append(main_character['ATK'])
      Character_DefaultATK.append(main_character['ATK'])
      Character_HP.append(main_character['HP'])
      Character_DefaultHP.append(main_character['HP'])
      availableskillpoints.append(main_character['Skillpoints'])
      Character_Role.append(main_character['Role'])
      Character_Status.append("Alive")
      print("Welcome to the tutorial", Character)
 def Available_Enemies(data):
  for basic_enemies in data:
   X = int(''.join(map(str, Character_HP)))
   if X > basic_enemies['HP']:
    All_Enemies.append(basic_enemies['Name'])
 def Search_EnemyName(data):
  E = input("Input Enemy Name: ")
  if E in All_Enemies:
   for basic_enemies in data:
    if E in basic_enemies['Name'] :
     Enemy.append(basic_enemies['Name'])
     Enemy_HP.append(basic_enemies['HP'])
     Enemy_ATK.append(basic_enemies['ATK'])
     Can_Fight.append("Yes")
  else:
    print("You cannot fight a", E)
    Can_Fight.append("No")
 def enemy_attack():
    x = int(''.join(map(str, Enemy_ATK)))
    y = int(''.join(map(str, Character_HP)))
    finalhp = (y - x)
    if 0 >= finalhp:
       print("You are dead")
       X = "Dead"
       Character_Status.clear()
       Character_Status.append(X)
    else:
     Character_HP.clear()
     Character_HP.append(finalhp)
     print (Character,"has",finalhp,"HP remaining")
 def attack():
    x = int(''.join(map(str, Enemy_HP)))
    y = int(''.join(map(str, Character_ATK)))
    finalhp = (x - y)
    if finalhp <= 0:
       print("The Enemy is dead")
       X = "Dead"
       Status.clear()
       Status.append(X)
    else:
     Enemy_HP.clear()
     Enemy_HP.append(finalhp)
     print ("The",Enemy,"has",finalhp,"HP remaining")
 def enhance_attack():
    X = input("how much energy do you want to use? ")
    Y = int(X)
    Input.clear()
    Input.append(Y)
    if Input > Character_Energy:
        print ("You don't have enough energy!")
    else:
        x = int(''.join(map(str, Input)))
        y = int(''.join(map(str, Character_ATK)))
        Final_ATK = (x + y)
        Character_ATK.clear()
        Character_ATK.append(Final_ATK)
        print("Your new attack is:", Final_ATK)
        w = int(''.join(map(str, Input)))
        v = int(''.join(map(str, Character_Energy)))
        W = (v - w)
        Character_Energy.clear()
        Character_Energy.append(W)
        print("You have", Character_Energy, "energy remaining")
 def heal():
    X = input("how much energy do you want to use? ")
    Y = int(X)
    Input2.clear()
    Input2.append(Y)
    if Input2 > Character_Energy:
        print ("you don't have enough energy!")
    else:
        x = int(''.join(map(str, Input2)))
        y = int(''.join(map(str, Character_HP)))
        Final_HP = (x + y)
        Character_HP.clear()
        Character_HP.append(Final_HP)
        print("Your new HP is:", Final_HP)
        w = int(''.join(map(str, Input2)))
        v = int(''.join(map(str, Character_Energy)))
        W = (v - w)
        Character_Energy.clear()
        Character_Energy.append(W)
        print("You have", Character_Energy, "energy remaining")
 def retreat():
    print ("Retreating from battle (imagine being a scaredy cat)")
 def exit_game():
    print("Note: Your progress will not be saved as you should be finishing this game in one sitting")

class skill_point():
 def use_skillpoint():
    print("Skillpoints:", availableskillpoints)
    X = input("how much skill points do you want to use? ")
    Input3.clear()
    Input3.append(X)
    c = int(''.join(map(str, availableskillpoints)))
    d = int(''.join(map(str, Input3)))
    if d > c:
         print ("You don't have enough skill points!")
    else:
        S = input("Which stat do you want to improve? (HP, ATK, ENERGY) ")
        if S == 'HP':
         x = int(''.join(map(str, Character_DefaultHP)))
         y = int(''.join(map(str, Character_DefaultATK)))
         z = int(''.join(map(str, Character_DefaultEnergy)))
         a = int(''.join(map(str, Input3)))
         New = x + (a*20)
         Character_DefaultHP.clear()
         Character_ATK.clear()
         Character_Energy.clear()
         Character_DefaultHP.append(New)
         Character_HP.clear()
         Character_HP.append(New)
         Character_ATK.append(y)
         Character_Energy.append(z)
         print("New HP is:",New)
        elif S == 'ATK':
         x = int(''.join(map(str, Character_DefaultHP)))
         y = int(''.join(map(str, Character_DefaultATK)))
         z = int(''.join(map(str, Character_DefaultEnergy)))
         b = int(''.join(map(str, Input3)))
         New = y + (b*20)
         Character_DefaultATK.clear()
         Character_HP.clear()
         Character_Energy.clear()
         Character_DefaultATK.append(New)
         Character_ATK.clear()
         Character_ATK.append(New)
         Character_HP.append(x)
         Character_Energy.append(z)
         print("New ATK is:",New)
        elif S == 'ENERGY':
         x = int(''.join(map(str, Character_DefaultHP)))
         y = int(''.join(map(str, Character_DefaultATK)))
         z = int(''.join(map(str, Character_DefaultEnergy)))
         c = int(''.join(map(str, Input3)))
         New = z + (c*15)
         Character_DefaultEnergy.clear()
         Character_ATK.clear()
         Character_HP.clear()
         Character_DefaultEnergy.append(New)
         Character_Energy.clear()
         Character_Energy.append(New)
         Character_ATK.append(y)
         Character_HP.append(x)
         print("New Energy is:",New)
        F = c - d
        availableskillpoints.clear()
        availableskillpoints.append(F)

def actual_fighting():
 All_Enemies.clear()
 combat.Available_Enemies(data)
 print("These are the enemies you can fight", All_Enemies)
 Enemy.clear()
 Enemy_HP.clear()
 Enemy_ATK.clear()
 Status.append("Alive")
 combat.Search_EnemyName(data)
 if Can_Fight == ['Yes']:
  while input:
   print("1 = [attack], 2 = [enhance attack], 3 = [heal], 4 = [retreat], 5 = [exit game]")
   X = input()
   if X == '1':
    combat.attack()
    if Status == ['Dead']:
      Status.clear()
      I = int(''.join(map(str, availableskillpoints)))
      New = I + 1
      availableskillpoints.clear()
      availableskillpoints.append(New)
      Ask = input("Do you want to use your skillpoints? (Y/N) ")
      if Ask == 'Y':
        skill_point.use_skillpoint()
        actual_fighting()
      if Ask == 'N':
       x = int(''.join(map(str, Character_DefaultHP)))
       y = int(''.join(map(str, Character_DefaultATK)))
       z = int(''.join(map(str, Character_DefaultEnergy)))
       Character_ATK.clear()
       Character_HP.clear()
       Character_Energy.clear()
       Character_ATK.append(y)
       Character_HP.append(x)
       Character_Energy.append(z)
       actual_fighting()
    elif Status == ['Alive']:
     combat.enemy_attack()
     if Character_Status == ['Dead']:
      Character_Status.clear()
      print("You suck at this!!!")
      Ask = input("Do you want to use your skillpoints? (Y/N) ")
      if Ask == 'Y':
        skill_point.use_skillpoint()
        x = int(''.join(map(str, Character_DefaultHP)))
        y = int(''.join(map(str, Character_DefaultATK)))
        z = int(''.join(map(str, Character_DefaultEnergy)))
        Character_ATK.clear()
        Character_HP.clear()
        Character_Energy.clear()
        Character_ATK.append(y)
        Character_HP.append(x)
        Character_Energy.append(z)
        actual_fighting()
      if Ask == 'N':
       x = int(''.join(map(str, Character_DefaultHP)))
       y = int(''.join(map(str, Character_DefaultATK)))
       z = int(''.join(map(str, Character_DefaultEnergy)))
       Character_ATK.clear()
       Character_HP.clear()
       Character_Energy.clear()
       Character_ATK.append(y)
       Character_HP.append(x)
       Character_Energy.append(z)
       actual_fighting()
       break
   elif X == '2':
    combat.enhance_attack()
    combat.enemy_attack()
    if Character_Status == ['Dead']:
      Character_Status.clear()
      print("You suck at this!!!")
      Ask = input("Do you want to use your skillpoints? (Y/N) ")
      if Ask == 'Y':
        skill_point.use_skillpoint()
        x = int(''.join(map(str, Character_DefaultHP)))
        y = int(''.join(map(str, Character_DefaultATK)))
        z = int(''.join(map(str, Character_DefaultEnergy)))
        Character_ATK.clear()
        Character_HP.clear()
        Character_Energy.clear()
        Character_ATK.append(y)
        Character_HP.append(x)
        Character_Energy.append(z)
        actual_fighting()
      if Ask == 'N':
       x = int(''.join(map(str, Character_DefaultHP)))
       y = int(''.join(map(str, Character_DefaultATK)))
       z = int(''.join(map(str, Character_DefaultEnergy)))
       Character_ATK.clear()
       Character_HP.clear()
       Character_Energy.clear()
       Character_ATK.append(y)
       Character_HP.append(x)
       Character_Energy.append(z)
       actual_fighting()
   elif X == '3':
    combat.heal()
    combat.enemy_attack()
    if Character_Status == ['Dead']:
      Character_Status.clear()
      print("You suck at this!!!")
      Ask = input("Do you want to use your skillpoints? (Y/N) ")
      if Ask == 'Y':
        skill_point.use_skillpoint()
        x = int(''.join(map(str, Character_DefaultHP)))
        y = int(''.join(map(str, Character_DefaultATK)))
        z = int(''.join(map(str, Character_DefaultEnergy)))
        Character_ATK.clear()
        Character_HP.clear()
        Character_Energy.clear()
        Character_ATK.append(y)
        Character_HP.append(x)
        Character_Energy.append(z)
        actual_fighting()
      if Ask == 'N':
       x = int(''.join(map(str, Character_DefaultHP)))
       y = int(''.join(map(str, Character_DefaultATK)))
       z = int(''.join(map(str, Character_DefaultEnergy)))
       Character_ATK.clear()
       Character_HP.clear()
       Character_Energy.clear()
       Character_ATK.append(y)
       Character_HP.append(x)
       Character_Energy.append(z)
       actual_fighting()
   elif X == '4':
    combat.retreat()
    actual_fighting()
   elif X == '5':
    combat.exit_game()
    Why = input("Confirm to exit game? (Y/N) ")
    if Why == 'N':
     actual_fighting()
    if Why == 'Y':
     exit()
 else:
  Can_Fight.clear()

Status.clear()
Character_Status.clear()
combat.Search_CharacterName(cdata)
actual_fighting()