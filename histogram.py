import string
# from collections import defaultdict
from radixtree import RadixTree


class Histogram:
    def __init__(self):
        self._tree = RadixTree()

    def frequency(self, word):
        return self._tree.search(word)

    def entries(self):
        return self._tree.count

    def unique_words(self):
        return len([freq for _, freq in self._tree.get_words() if freq == 1])

    def add_word(self, word):
        self._tree.insert(word)

    def load_from_file(self, filename):
        words = get_words_from_file(filename)
        self.load_from_list(words)

    def load_from_list(self, words):
        for word in words:
            self._tree.insert(word)


def get_words_from_file(name):
    bad = string.punctuation + "\n"
    table = str.maketrans(bad, " "*len(bad))
    words = []
    with open("data/downandout.txt", 'r') as f:
        for i in f:
            if i == "\n":
                continue
            words.extend(i.translate(table).strip().lower().split(" "))
    words = [i for i in words if i.strip() != ""]
    return words


if __name__ == "__main__":
    myHistogram = Histogram()
    myHistogram.load_from_file("data/downandout.txt")
    print("frequency of 'the': ", myHistogram.frequency("the"))
    print("unique_words(): ", myHistogram.unique_words())
    print("entries(): ", myHistogram.entries())
