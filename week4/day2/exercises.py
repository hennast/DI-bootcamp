my_fav_numbers = {7,6,8}
my_fav_numbers.add(9)
my_fav_numbers.add(4)
print(my_fav_numbers)
friend_fav_numbers = {9, 2, 4}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#exercise 2
#Given a tuple which value is integers, is it possible to add more integers to the tuple?
#no
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("kiwi")
basket.insert(0, "Apples")
apples_amount = []
x  = 0
for fruit in basket:
    if basket[x] == "Apples":
        apples_amount.append(basket[x])
    x += 1
print(len(apples_amount))
basket.clear()
print(basket)

numbers = (range(1, 21))

for number in numbers:
    print(number)
for number in numbers:
    if number % 2 == 0:
        print(number)

my_name = ""
while my_name != "henna":
    my_name = input("what is your name")


user_fave_fruits = input("what is your favorite fruit")
fav_fruits = user_fave_fruits.split(" ")
print(fav_fruits)
new_fruit = input("name a fruit")
if new_fruit in fav_fruits:
    print("you chose a great fruit")
else:
    print("you chose a new fruit")