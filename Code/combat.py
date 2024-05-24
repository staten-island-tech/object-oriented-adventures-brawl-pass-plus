import json
enemies = open("enemyinfo.json", encoding="utf8")
character = open("characterinfo.json", encoding="utf8")
data = json.load(enemies)
cdata = json.load(character)

Character = []
Enemy = []
Enemy_HP = []
Enemy_ATK = []
Character_Energy = []
Character_ATK = []
Character_HP = []
Input = []
Input2 = []
Status = []
Character_Status = []

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
    Enemy_ATK.append(basic_enemies['ATK'])
    print("Welcome to the tutorial", Character)
 def enemy_attack():
    x = int(''.join(map(str, Enemy_ATK)))
    y = int(''.join(map(str, Character_HP)))
    finalhp = (y - x)
    if 0 >= finalhp:
       print("You are dead")
       X = "Dead"
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
        print ("you don't have enough energy!")
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
    print ("Exiting game...")

Status.clear()
combat.Search_CharacterName(cdata)
combat.Search_EnemyName(data)
while input:
 print("1 = [attack], 2 = [enhance attack], 3 = [heal], 4 = [retreat], 5 = [exit game]")
 X = input()
 if X == '1':
    combat.attack()
    combat.enemy_attack()
    if Status == ['Dead']:
       break
    if Character_Status == ['Dead']:
       print("You suck at this!!!")
       break
 elif X == '2':
    combat.enhance_attack()
    combat.enemy_attack()
    if Character_Status == ['Dead']:
       print("You suck at this!!!")
       break
 elif X == '3':
    combat.heal()
    combat.enemy_attack()
    if Character_Status == ['Dead']:
       print("You suck at this!!!")
       break
 elif X == '4':
    combat.retreat()
    print("Deleting save...")
    print("Note: Come back when you gain some courage.")
    break
 elif X == '5':
    combat.exit_game()

class skill_point():
    def skillpoints(HP, ATK, ENERGY):
        HP = 20
        ATK = 20
        ENERGY = 15
    X = input("how much skill points do you want to use? ")
    skillpoints_used.append(X)
    if skillpoints_used > availableskillpoints:
        print ("you don't have enough skill points!")
    else: 
        from Beginning import CharacterFinder2
        S = input("Which stat do you want to improve? HP, ATK, ENERGY ")
        if S == 'HP':
            while():
                CharacterFinder2.Search_CharacterName(data)
            for main_character in data:
                print("HP:",main_character['HP'])
                break
        elif S == 'ATK':
            while():
                CharacterFinder2.Search_CharacterName(data)
            for main_character in data:
                print("HP:",main_character['ATK'])
        elif S == 'ENERGY':
            while():
                CharacterFinder2.Search_CharacterName(data)
            for main_character in data:
                print("HP:",main_character['ENERGY'])
                break
