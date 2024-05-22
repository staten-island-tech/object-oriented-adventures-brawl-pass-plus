availableskillpoints = {}
availableskillpoints = 1
skillpoints_used = {}
class skill_points():
    def skillpoints(HP, ATK, ENERGY):
        HP = ("20")
        ATK = ("10")
        ENERGY = ("15")
    X = input("how much skill points do you want to use? ")
    X.append(skillpoints_used)
    if skillpoints_used > availableskillpoints:
        print ("you don't have enough skill points!")
    else:
        F = input("Open A Previous Save? (Y/N)")
        if F == 'Y':
            from Beginning import CharacterFinder
            CharacterFinder.Search_CharacterName()