string = input("please input a sentence")
amountOfOccurences = 0
letterToCheck = input ("pick one letter")
for element in string:
    if element == letterToCheck:
        amountOfOccurences += 1
print(amountOfOccurences)
