number = input('please input a number')
number = int(number)
length = input('please input a length')
length = int(length)
current_number= 1
multiplied = []
while current_number <= length:
    number = number * current_number
    current_number += 1
    multiplied.append(number)
print(multiplied)