import string


class Histogram():
    def __init__(self, filename):
        words = getWordsFromFile(filename)
        hist = {}
        for i in words:
            if i in hist.keys():
                hist[i] += 1
            else:
                hist[i] = 1
        self.histogram = hist

    def frequency(self, word):
        if word not in self.histogram.keys():
            return 0
        else:
            return self.histogram[word]

    def unique_words(self):
        return sum([i for i in self.histogram.values() if i == 1])


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
