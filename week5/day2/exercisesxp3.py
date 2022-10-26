
from exercises import Dog
import random

class Pet_Dog(Dog):
    pass
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        self.bark()
        self.trained = True
    def play(self, *args):
        print(f'{args} play together')
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        trick = random.choice(tricks)
        if self.trained == True:
            print(f'{self.name} {trick}')

class Dalmation(Pet_Dog):
    pass
dalmation = Dalmation("dog", 4, 14)
dalmation.train()
dalmation.do_a_trick()