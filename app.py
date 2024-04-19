class mobs():
    def __init__(self, name):
        self.name = name

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
        name = "Slime"
        atk = 5
        hp = 50

class goblin(basicenemies):
    def __init__(self):
        name = "Goblin"
        atk = 10
        hp = 75

class speargoblin(basicenemies):
    def __init__(self):
        name = "Spear Goblin"
        atk = 12
        hp = 60