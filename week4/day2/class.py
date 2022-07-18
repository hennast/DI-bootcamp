from gettext import find


list = [1, 2, 3, 4]
multiply = 1
for number in list:
    multiply = multiply * number
print(multiply)

find_20 = [5, 10, 15, 20, 25, 30]
idx = find_20.index(20)
find_20[idx]= 200
print(find_20)


