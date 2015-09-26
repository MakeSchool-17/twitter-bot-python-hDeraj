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

    def load_from_file(self, filename):
        words = get_words_from_file(filename)
        self.load_from_list(words)

    def load_from_list(self, stuff):
        for i in stuff:
            self.add_word(i)


def get_words_from_file(name):
    table = str.maketrans("", "", string.punctuation + "\n")
    words = []
    with open("data/downandout.txt", 'r') as f:
        for i in f:
            if i == "\n":
                continue
            words.extend(i.strip().translate(table).split(" "))
    return words


if __name__ == "__main__":
    myHistogram = Histogram("data/downandout.txt")
    print(myHistogram.frequency("the"))
    print(myHistogram.unique_words())
    print(len(myHistogram.histogram.keys()))
