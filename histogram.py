from radixtree import RadixTree


class Histogram:
    def __init__(self, tree_class=RadixTree):
        self._tree = tree_class()

    def frequency(self, word):
        return self._tree.search(word)

    def entries(self):
        return self._tree.count

    def unique_words(self):
        return len([freq for _, freq in self._tree.get_words() if freq == 1])

    def add_word(self, word):
        self._tree.insert(word)

    def load_from_list(self, words):
        for word in words:
            self._tree.insert(word)
