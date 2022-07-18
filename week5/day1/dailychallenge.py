from mimetypes import init
from unicodedata import name

animals = {}
class Farm:
    def __init__(self,name):
        self.name = name
        
    def add_animal(self, animal, quantity = 1):
        if animal in animals.keys():
            animals[animal] =+ int(quantity)
        else:
            animals[animal] = quantity
    def get_info(self):
        return (f'{animals} eieio')
        

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())