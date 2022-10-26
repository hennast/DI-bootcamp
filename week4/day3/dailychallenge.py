from re import L


user_word = input('please input a word')
idx = enumerate(user_word)
new_dict = dict(zip(user_word,idx))
word_dictionary = {}
for index, letter in enumerate(user_word):
    if letter in word_dictionary.keys():
        word_dictionary[letter].append(index)
    else:
        word_dictionary[letter] = [index]
    print(letter)
print(word_dictionary)

#2
items_purchase = {
  'Water': 1,
  'Bread': 3,
  'TV': 1000,
  'Fertilizer': 20
}
wallet = input('how much is in your wallet')
wallet = int(wallet)
print(wallet)
you_can_afford = []
for value, price in items_purchase.items():
    price = int(price)
    if wallet > price:
        you_can_afford.append(items_purchase.keys())

print(you_can_afford.sort())
