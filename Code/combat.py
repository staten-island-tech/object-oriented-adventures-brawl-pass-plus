import json
enemies = open("enemyinfo.json", encoding="utf8")
character = open("characterinfo.json", encoding="utf8")
data = json.load(enemies)
cdata = json.load(character)

class battle():
    def __init__(self,combat, enemycombat):
        self.combat = combat
        self.enemycombat = enemycombat
class combat(battle):
    def attack(cdata):
        if "Slime" in enemies['Name']:
         HP = enemies['HP']
         ATK = character['ATK']
         print(HP - ATK)
    def enhance_attack(cdata):
            print ("how much energy do you want to use")
            if input >= character ["ENERGY"]:
                print ("you don't have enough energy")
            else:
                input + character ["ATK"]
    def heal(cdata):
            print ("how much energy do you want to use")
            if input >= character ["ENERGY"]:
                print ("you don't have enough energy")
            else:
                input + character ["HP"]
    def retreat():
            print ("retreating from battle")
    def exit_game():
            print ("exiting game")


""" class enemycombat(battle):
    while battle:
        print("A ", enemies["Name"], " has spawned")
        character["HP"] - enemies["ATK"]
        print ("the enemy did ", enemies["ATK"], "dmg to you and you have ", character["HP"], "Hp remaining")
        if enemies["HP"] == 0:
            break
        print("Battle Won") """

print("1 attack 2 enhance attack 3 heal 4 retreat 5 exit game")
x = input()
if x == '1':
    combat.attack(cdata)
elif x == '2':
    combat.enhance_attack(cdata)
elif x == '3':
    combat.heal(cdata)
elif x == '4':
    combat.retreat()
elif x == '5':
    combat.exit_game()
