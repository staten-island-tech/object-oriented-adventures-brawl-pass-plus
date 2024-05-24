import json
enemies = open("enemyinfo.json", encoding="utf8")
data = json.load(enemies)
character = open("characterinfo.json", encoding="utf8")
cdata = json.load(character)

while input:
 from Combat import combat
 X = input()
 if X == '1':
    combat.attack()
 elif X == '2':
    combat.enhance_attack()
 elif X == '3':
    combat.heal()
 elif X == '4':
    combat.retreat()
    break
 elif X == '5':
    combat.exit_game()
    break
