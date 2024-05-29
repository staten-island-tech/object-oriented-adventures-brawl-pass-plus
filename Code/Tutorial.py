import json
enemies = open("enemyinfo.json", encoding="utf8")
data = json.load(enemies)
character = open("characterinfo.json", encoding="utf8")
cdata = json.load(character)
class tutorial():
    print ("Welcome to the tutorial, in this game you can choose the enemy you want to fight but be warned as some enemy can easily kil you so choose who you want to fight wisely")
    print ("For every enemy you kill you will gain one skill point, each skill point will buff your")
    print ("HP by 20")
    print ("ATK by 20")
    print ("ENERGY by 15")
