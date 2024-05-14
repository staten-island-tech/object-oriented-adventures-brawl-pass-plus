import json
enemies = open("enemyinfo.json", encoding="utf8")
data = json.load(enemies)
character = open("characterinfo.json", encoding="utf8")
cdata = json.load(character)

class CharacterFinder():
    def Search_CharacterName(cdata):
        Z = input("Input Character Name: ")
        for main_character in cdata:
            if Z in main_character['Name'] :
                print("Welcome to the tutorial", main_character["Name"])


class combat():
 def Search_CharacterName(cdata):
    Z = input("Input Character Name: ")
    for main_character in cdata:
     if Z in main_character['Name'] :
      print("Welcome to the tutorial", main_character["Name"])
 def Search_EnemyName(data):
  E = input("Input Enemy Name: ")
  for basic_enemies in data:
   if E in basic_enemies['Name'] :
    print("Name:",basic_enemies['Name'])
    print("HP:",basic_enemies['HP'])
    print("ATK:",basic_enemies['ATK']) 
    basic_enemies = enemies
 def attack():
    E = input("Input Enemy Name: ")
    Z = input("Input Character Name: ")
    for basic_enemies in data:
        for main_character in cdata:
            if Z in main_character['Name']:
                if E in basic_enemies['Name']:
                    x = (basic_enemies["HP"])
                    y = (main_character["ATK"])
                    finalhp = x - y
                    print (finalhp)
    
 def enhance_attack():
    input ("how much energy do you want to use")
    if input >= character ["ENERGY"]:
        print ("you don't have enough energy")
    else:
        input + character ["ATK"]
 def heal():
    print ("how much energy do you want to use")
    if input >= character ["ENERGY"]:
        print ("you don't have enough energy")
    else:
        input + character ["HP"]
 def retreat():
    print ("retreating from battle")
 def exit_game():
    print ("exiting game")

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
