import string


class Histogram:
    def __init__(self):
        self.histogram = {}

    def frequency(self, word):
        if word not in self.histogram.keys():
            return 0
        else:
            return self.histogram[word]

    def unique_words(self):
        return sum([i for i in self.histogram.values() if i == 1])

    def loadFromFile(self, filename):
        words = getWordsFromFile(filename)
        for i in words:
            if i in self.histogram.keys():
                self.histogram[i] += 1
            else:
                self.histogram[i] = 1

    def loadFromList(self, stuff):
        for i in stuff:
            if i in self.histogram.keys():
                self.histogram[i] += 1
            else:
                self.histogram[i] = 1


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

    print("nothing")
