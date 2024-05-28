import json
enemies = open("enemyinfo.json", encoding="utf8")
data = json.load(enemies)
character = open("characterinfo.json", encoding="utf8")
cdata = json.load(character)

print ("Welcome to the tutorial, in this game you can choose the enemy you want to fight but be warned as some enemy can easily kil you so choose who you want to fight wisely")
from combat import combat