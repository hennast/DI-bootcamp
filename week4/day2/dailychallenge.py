number = input('please input a number')
number = int(number)
length = input('please input a length')
length = int(length)
current_number= 1
multiplied = []
while current_number <= length:
    x = 1
    x = number * current_number
    current_number += 1
    multiplied.append(x)
print(multiplied)



user_string = input('please input a word')
user_string = user_string + " "
x = 1
# no_duplicates = set()
word = ""

while x < len(user_string):
    if user_string[x-1] != user_string[x]:
        word = word + user_string [x-1]
    x += 1

print(word)

