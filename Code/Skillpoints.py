availableskillpoints = ["1"]
skillpoints_used = [""]
class skill_point():
    def skillpoints(HP, ATK, ENERGY):
        HP = 20
        ATK = 20
        ENERGY = 15
    X = input("how much skill points do you want to use? ")
    skillpoints_used.append(X)
    if skillpoints_used > availableskillpoints:
        print ("you don't have enough skill points!")
    else: 
        S = input("Which stat do you want to improve? HP, ATK, ENERGY ")
        if S == 'HP':
            CharacterFinder.Search_CharacterName()
        elif S == 'ATK':
            CharacterFinder.Search_CharacterName()
        elif S == 'ENERGY':
            CharacterFinder.Search_CharacterName()