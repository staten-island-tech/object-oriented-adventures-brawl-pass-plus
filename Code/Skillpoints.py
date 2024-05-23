availableskillpoints = 1
skillpoints_used = []
class skill_points():
    def skillpoints(HP, ATK, ENERGY):
        HP = 20
        ATK = 10
        ENERGY = 15
    X = int(input("how much skill points do you want to use? "))
    skillpoints_used.append(X)
    if skillpoints_used > availableskillpoints:
        print ("you don't have enough skill points!")
    else: 
        S = input("Which stat do you want to improve? Hp, ATK, ENERGY")
        if S == 'HP':
            from Beginning import CharacterFinder
            CharacterFinder.Search_CharacterName()
        elif S == 'ATK':
            from Beginning import CharacterFinder
            CharacterFinder.Search_CharacterName()
        elif S == 'ENERGY':
            from Beginning import CharacterFinder
            CharacterFinder.Search_CharacterName()