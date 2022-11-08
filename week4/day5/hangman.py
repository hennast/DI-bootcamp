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

def check_letter(Theword):
    global blank, extr
    not_in_word = 0
    letter = input("please input a letter")
    if letter in Theword:
        idx = Theword.index(letter)
        blank = list(blank)
        (blank)[idx] = letter
        blank = "".join(blank)
    else:
        not_in_word+=1 #keeps track of bad guesses
        extr.append(letter)
    print(blank)
    print(extr)
    return blank, extr

  

while word != blank:
    check_letter(word)

