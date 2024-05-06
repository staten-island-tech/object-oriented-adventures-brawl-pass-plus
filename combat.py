import json
enemies = open("enemyinfo.json", encoding="utf8")
data = json.load(enemies)
character = open("characterinfo.json", encoding="utf8")
cdata = json.load(character)


class combat():
    print("1 attack 2 enhance attack 3 heal 4 retreat 5 exit game")
    def attack(cdata):
        if input == "1":
            character ["ATK"] - enemies ["HP"]
    def enhance_attack
