import json
enemies = open("enemyinfo.json", encoding="utf8")
data = json.load(enemies)
character = open("characterinfo.json", encoding="utf8")
cdata = json.load(character)

class battle():
    def __init__(self,combat, enemycombat):
        self.combat = combat
        self.enemycombat = enemycombat
class combat(battle):
    print("1 attack 2 enhance attack 3 heal 4 retreat 5 exit game")
    def attack(cdata):
        if input == "1":
            enemies ["HP"] - character ["ATK"]
    def enhance_attack(cdata):
        if input == "2":
            print ("how much energy do you want to use")
            if input >= character ["ENERGY"]:
                print ("you don't have enough energy")
            else:
                input + character ["ATK"]
    def heal(cdata):
        if input == "3":
            print ("how much energy do you want to use")
            if input >= character ["ENERGY"]:
                print ("you don't have enough energy")
            else:
                input + character ["HP"]
    def retreat():
        if input == "4":
            print ("retreating from battle")
    def exit_game():
        if input == "5":
            print ("exiting game")


class enemycombat(battle):
    while battle:
        character["HP"] - enemies["ATK"]
        print ("the enemy did ", enemies["ATK"], " dmg to you and you have ", character["HP"], "Hp remaining")
        if enemies["HP"] == 0:
            break
        print("Battle Won")