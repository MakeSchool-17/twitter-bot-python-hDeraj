class RadixTree:
    def __init__(self, words=[]):
        self.roots = []
        self.numberOfWords = 0
        if len(words) > 0:
            self.load_words(words)

    def load_words(self, words):
        pass

    def search(self, word):
        pass

    def insert(self, word):
        pass

    def delete(self, word):
        pass


class RadixNode:
    def __init__(self, prefix=""):
        self.prefix = prefix
        self.children = []
        self.frequency = 0

    def is_leaf(self):
        return len(self.children) == 0


if __name__ == "__main__":
    print("RadixTree")
