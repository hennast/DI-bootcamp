class Character:
    def __init__(self, name, life = 20, attack = 10):
        self.name = name
        self.life = life
        self.attack = attack
        if self.life <= 0:
            print(self.name, " is dead")
    def basic_attack(self, Character):
        Character.life = Character.life - self.attack
    def print_stats(self):
        print("name: ", self.name)
        print("life: ", self.life)
        print("attack: ", self.attack)


#animal_help()- increases attack by 5
#fight() - accepts another Character instance as a parameter and subtracts (0.75*life + 0.75*attack) from the other character’s life.
#Example:
#druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)

class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("I am Druid")
    def meditate(self):
        self.life = self.life + 10
        self.attack = self.attack - 2
    def animal_help(self):
        self.attack = self.attack + 5
    def fight(self, Character):
        Character.life = Character.life - (0.75*self.life + 0.75*self.attack)
        print(Character.life)
 


#Warrior:
#brawl() - accepts another Character instance as a parameter, subtracts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
#train() - increases both your attack and life points by 2.
#roar() - accepts another Character instance as a parameter and subtracts their attack points by 3.

class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("HI I'm mr wizard aka", self.name)
    def brawl(self, Character):
        Character.life = Character.life - (2 * self.attack)
        self.attack = self.attack + (self.attack * .5)
    def train(self):
        self.attack += 2
        self.life += 2
    def roar(self, Character):
        Character.attack -= 3

#Mage:
#curse() – accepts another Character instance as a parameter and subtracts their attack points by 2.
#summon() - increases attack attribute by 3 points.
#cast_spell() - accepts another Character instance as a parameter and subtracts attack/life to the other character’s life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).

class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("Yo")
    def curse(self,Character):
        Character.attack -=2
    def summon(self):
        self.attack += 3
    def cast_spell(self, Character):
        Character.life = Character.life - (self.attack / self.life)


#my druids
bob = Druid("bobert")
jennofer = Druid("Jennofer", 26, 17)