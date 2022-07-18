class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'



class Siamese(Cat):
    pass

bengal = Bengal("henna", 1)
chartreaux = Chartreux('guy', 4)
siamese = Siamese("kitty", 8)

all_cats = [bengal, chartreaux, siamese]
saras_pets = Pets(all_cats)
saras_pets.walk()


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f'{self.name} barking'
    def run_speed(self):
        return int(self.weight) / int(self.age) * 10
    def fight(self, other_dog):
        running_speed = self.run_speed()
        if running_speed * self.weight > other_dog.run_speed() *other_dog.weight:
            print(f'{self.name} is the winner')
        else:
            print(f'{other_dog.name} is the winner')        
class Sheperd(Dog):
    pass
class Husky(Dog):
    pass
class Poodle(Dog):
    pass

sheperd = Sheperd("morgan",2, 40)
husky = Husky("amy", 4, 50)
poodle = Poodle("oreo", 1, 15)
#all_dogs = [sheperd, husky]
#in_fight = Dog(all_dogs
husky.fight(sheperd)
    

