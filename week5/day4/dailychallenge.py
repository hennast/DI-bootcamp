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
    def dictionary(self):
        #creates a dictionary of how many times each word
        stringAslist = self.string.split(" ")
        for word in stringAslist:
            if word in StringDict.keys():
                StringDict[word] += 1
            else:
                StringDict[word] = 1
        return self.dictionary
    def mostCommon(self):
        #a method that returns the most common word in the text.
        global StringDict
        self.dictionary()
        x = 0
        mostCommonWord = ""
        for key, value in StringDict.items():
            if value > x:
                x = value
                mostCommonWord = key
            else:
                pass
        print(f"the most common word is {mostCommonWord} which appears {x} times")
        StringDict = {}
        return StringDict
    def unique(self):
        #a method that returns a list of all the unique words in the text.
        global StringDict
        self.dictionary()
        uniqueWords = []
        for key, value in StringDict.items():
            if value == 1:
                uniqueWords.append(key)
            else:
                pass
        print(uniqueWords)
        StringDict = {}
        return StringDict

test = Text(sampleSentence)
test.count("good")
test.mostCommon()
test.unique()





