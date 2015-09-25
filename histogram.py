import string
from collections import defaultdict


class Histogram:
    def __init__(self):
        self.histogram = defaultdict(int)
        self.items = 0

    def frequency(self, word):
        return self.histogram[word]

    def unique_words(self):
        return sum([i for i in self.histogram.values() if i == 1])

    def add_word(self, word):
        self.histogram[word] += 1
        self.items += 1

    def loadFromFile(self, filename):
        words = getWordsFromFile(filename)
        for i in words:
            self.add_word(i)

    def loadFromList(self, stuff):
        for i in stuff:
            self.add_word(i)


def getWordsFromFile(name):
    f = open("data/downandout.txt", 'r')
    lines = f.readlines()
    f.close()
    table = str.maketrans("", "", string.punctuation + "\n")
    words = []
    for i in lines:
        if i == "\n":
            continue
        words.extend(i.translate(table).split(" "))
    print(words[:100])
    return words


if __name__ == "__main__":
    myHistogram = Histogram("data/downandout.txt")
    print(myHistogram.frequency("the"))
    print(myHistogram.unique_words())
    print(len(myHistogram.histogram.keys()))
