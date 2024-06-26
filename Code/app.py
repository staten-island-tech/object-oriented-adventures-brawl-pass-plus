class mobs():
    def __init__(self, name):
        self.name = name

class stats():
    def __init__(self, atk, hp, energy):
        self.atk = atk
        self.hp = hp
        self.energy = energy

class basicenemies(mobs):
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

class minibosses(mobs):
    def __init__(self, name, atk, hp, skill):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.skill = skill

class bosses(mobs):
    def __intit__(self, name, atk, hp, skill):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.skill = skill

class slime(basicenemies):
    def __init__(self):
        self.name = "Slime"
        self.atk = 5
        self.hp = 50

class goblin(basicenemies):
    def __init__(self):
        self.name = "Goblin"
        self.atk = 10
        self.hp = 75

class speargoblin(basicenemies):
    def __init__(self):
        self.name = "Spear Goblin"
        self.atk = 12
        self.hp = 60

class skeleton(basicenemies):
    def __init__(self):
        self.name = "Skeleton"
        self.atk = 20
        self.hp = 100

class ghost(basicenemies):
    def __init__(self):
        self.name = "Ghost"
        self.atk = 15
        self.hp = 80

class wizard(basicenemies):
    def __init__(self):
        self.name = "Wizard"
        self.atk = 35
        self.hp = 75

class witch(basicenemies):
    def __init__(self):
        self.name = "Witch"
        self.atk = 40
        self.hp = 70

class knight(basicenemies):
    def __init__(self):
        self.name = "Knight"
        self.atk = 20
        self.hp = 150

class archer(basicenemies):
    def __init__(self):
        self.name = "Archer"
        self.atk = 55
        self.hp = 80

class goblinshaman(minibosses):
    def __init__(self):
        self.name = "Goblin Shaman"
        self.atk = 20
        self.hp = 225

class vengefulspirit(minibosses):
    def __init__(self):
        self.name = "Vengeful Spirit"
        self.atk = 100
        self.hp = 25

class hydra(minibosses):
    def __init__(self):
        self.name = "Hydra"
        self.atk = 20*9
        self.hp = 30*9

class dragon(minibosses):
    def __init__(self):
        self.name = "Dragon"
        self.atk = 100
        self.hp = 100

class archmage(minibosses):
    def __init__(self):
        self.name = "Arch Mage"
        self.atk = 5
        self.hp = 100

class paladin(minibosses):
    def __init__(self):
        self.name = "Paladin"
        self.atk = 50
        self.hp = 200

class royalguard(minibosses):
    def __init__(self):
        self.name = "Royal Guard"
        self.atk = 75
        self.hp = 100

