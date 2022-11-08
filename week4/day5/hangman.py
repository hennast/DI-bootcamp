import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) #this is the word that needs to be guessed from random list
blank = "" #this is the legth of the word given to user
x = 0 
while x < len(word):       
    blank = blank + "_"
    x+=1
print(blank)
extr = [] #empty array for guesses that arent in the word
not_in_word = 0

def check_letter(Theword = word):
    global blank, extr
    letter = input("please input a letter")
    if letter in Theword:
        blank = list(blank)
        Theword = list(Theword)
        for idx, value in enumerate(Theword):
            if value == letter:
                #idx = Theword.index(letter)
                blank[idx] = letter
        blank = "".join(blank)
    else:
        extr.append(letter)
    print(blank)
    print(extr)
    print(len(extr))
    return blank, extr

  

while word != blank:
    check_letter()
    if len(extr) == 5:
        print("you have lost the game")
        break
if word == blank:
    print("you have won the game")
