sampleSentence = "A good book would sometimes cost as much as a good house."
#Create a class called Text that takes a string as an argument and store the text in a attribute.
StringDict = {}
class Text:
    def __init__(self, string: str) -> None:
        self.string = string
    def count(self, word):
        #a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
        timesInString = 0
        stringAslist = self.string.split(" ")
        for value in stringAslist:
            if value == word:
                timesInString += 1
            else:
                pass
        if timesInString == 0:
            print(None)
        else:
            print(f"your word was found {timesInString} times")
    def dictionary(self, dictionary):
        #creates a dictionary of how many times each word
        stringAslist = self.string.split(" ")
        for word in stringAslist:
            if word in dictionary.keys():
                dictionary[word] += 1
            else:
                dictionary[word] = 1
        return self.dictionary
    def mostCommon(self, dictionary: dict):
        #a method that returns the most common word in the text.
        x = 0
        mostCommonWord = ""
        for key, value in dictionary.items():
            if value > x:
                x = value
                mostCommonWord = key
            else:
                pass
        print(f"the most common word is {mostCommonWord} which appears {x} times")
    def unique(self, dictionary: dict):
        #a method that returns a list of all the unique words in the text.
        uniqueWords = []
        for key, value in dictionary.items():
            if value == 1:
                uniqueWords.append(key)
            else:
                pass
        print(uniqueWords)

test = Text(sampleSentence)
test.count("good")
test.dictionary(StringDict)
test.mostCommon(StringDict)
test.unique(StringDict)





