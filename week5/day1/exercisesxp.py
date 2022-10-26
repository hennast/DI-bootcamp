# 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age



tabby = Cat("tabitha", 2)
tiger = Cat("tigger", 4)
lion = Cat("leo", 8)
cats =[tabby,tiger,lion]

for cat in cats:
    oldest_cat_age = 0
    oldest_cat = "cat"
    if cat.age > oldest_cat_age:
        oldest_cat_age = cat.age
        oldest_cat = cat.name
print(f'{oldest_cat} is the oldest')

#2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f'{self.name} goes woof')
    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high')
    

davids_dog = Dog("Rex", 50)
print(davids_dog.height)
print(davids_dog.name)
davids_dog.bark()
davids_dog.jump()
class Sarahs_dog(Dog):
    pass
sarahs_dog = Sarahs_dog("teacup", 20)

all_dogs = [sarahs_dog, davids_dog]
for dog in all_dogs:
    Biggest_dog_height = 0
    biggest_dog = ""
    if dog.height > Biggest_dog_height:
        Biggest_dog_height= dog.height
        biggest_dog = dog.name
print(f'{biggest_dog} is the biggest')



    
        