import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
blank = ""
x = 0
while x < len(word):       
    blank = blank + "_"
    x+=1
print(blank)


def check_letter(word,blank):
    extr = []
    not_in_word = 0
    letter = input("please input a letter")
    if letter in word:
        idx = word.index(letter)
        blank[idx] = letter
    else:
        not_in_word+=1
        extr.append(letter)
    print(blank)
    print(extr)
    
check_letter(word, blank)