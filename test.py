class roles():
  def __init__(Role, Warrior, Archer, Mage):
    Role.Warrior = Warrior
    Role.Archer = Archer
    Role.Mage = Mage
class main_character():
  def __init__(self, Role, Name, HP, ATK, ENERGY):
    self.Role = Role
    self.Name = Name
    self.HP = HP
    self.ATK = ATK
    self.ENERGY = ENERGY
class roles2(main_character):
  def Warrior(Role, Name, HP, ATK, ENERGY):
    Role.HP = "100"
    Role.ATK = "20"
    Role.ENERGY = "100"

    
        
Role == 'Warrior':
         HP = 120
         ATK = 20
         ENERGY = 100
         print(Name,"is an", Role)
         print("HP:", HP)
         print("ATK:", ATK)
         print("ENERGY:", ENERGY)
         main_character = main_character(Name, Role, HP, ATK, ENERGY)
      
         data.append(main_character.__dict__)
         break
       elif Role == 'Mage':
         HP = 80
         ATK = 10
         ENERGY = 200
         print(Name,"is an", Role)
         print("HP:", HP)
         print("ATK:", ATK)
         print("ENERGY:", ENERGY)
         main_character = main_character(Name, Role, HP, ATK, ENERGY)
         data.append(main_character.__dict__)
         break
       elif Role == 'Archer':
         role.Archer()
         HP = 100
         ATK = 15
         ENERGY = 150
         print(Name,"is an", Role)
         print("HP:", HP)
         print("ATK:", ATK)
         print("ENERGY:", ENERGY)
         main_character = main_character(Name, Role, HP, ATK, ENERGY)
         data.append(main_character.__dict__)


     