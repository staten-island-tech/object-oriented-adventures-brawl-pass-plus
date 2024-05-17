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
Input = []

class combat():
 def Search_CharacterName(cdata):
    Z = input("Input Character Name: ")
    for main_character in cdata:
     if Z in main_character['Name'] :
      Character.append(main_character['Name'])
      Character_Energy.append(main_character['ENERGY'])
      Character_ATK.append(main_character['ATK'])
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
                    print (finalhp)
 def enhance_attack():
    X = input("how much energy do you want to use? ")
    Y = int(X)
    Input.append(Y)
    print(Input)
    print(Character_Energy)
    if Input > Character_Energy:
        print ("you don't have enough energy!")
    else:
        print ("you have sufficient energy")
 def heal():
    print ("how much healing do you want to do? ")
    if input >= character ["ENERGY"]:
        print ("you don't have enough energy!")
    else:
        input + character ["HP"]
 def retreat():
    print ("retreating from battle (imagine being a scaredy cat)")
 def exit_game():
    print ("exiting game...")

combat.Search_CharacterName(cdata)
combat.Search_EnemyName(data)
print("1 attack 2 enhance attack 3 heal 4 retreat 5 exit game")
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
    combat.exit_game()

