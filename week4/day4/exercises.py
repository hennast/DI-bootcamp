#1
#def display_message():
   # """A function that says what you are learning"""
    #course = input("what are you learning")
    #print("I am learning", course) 

#display_message()

#2
from random import randint


def favorite_book(title):
    """a function that says the title of book"""
    print("one of my favorite books is", title)

favorite_book("alice in wonderland")

#3
def describe_city(city, country = "US"):
    print(city, "is in", country)

describe_city("new york", "fr")

#4
def random_number():
    print('number')

#5
def make_shirt(size = "large", message = "i love python"):
    print("The size of the shirt is", size, "and the text is", message)

make_shirt()
make_shirt("medium")
make_shirt("small")
make_shirt(message="hi")

#6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    print(magician_names)

show_magicians()

def make_great():
    x = 0
    for magician in magician_names:
       magician_names[x] = magician + " is great"
       x+= 1
    print(magician_names)

make_great()

def get_random_temp(season):
    if season == 'winter':
         return randint(-10, 7)
    elif season == 'spring':
        return randint(15, 23)
    elif season == 'fall':
        return randint(7, 15)
    elif season == 'summer':
        return randint(23, 40)
   
the_season = input('what season is it')   

def main():
    random_temp = get_random_temp(the_season)
    if random_temp < 0:
        print("its so cold")
    else:
        if random_temp < 16:
            print("it's pretty chilly")
        elif random_temp < 23:
            print("getting warmer")
        elif random_temp < 32:
            print("idk celsius")
        else:
            print("its hot")
    

main()