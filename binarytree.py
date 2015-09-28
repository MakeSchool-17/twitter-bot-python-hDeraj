class BinaryTree:
    def __init__(self):
        self.count = 0
        self.root = None

    def insert(self, word, count=1):
        self.count += count
        if not self.root:
            self.root = BinaryNode(word, count)
        else:
            self.root._insert(word, count)

    def search(self, word):
        if not self.root:
            return -1
        else:
            return self.root._search(word)

    def get_words(self):
        if not self.root:
            return []
        else:
            return self.root._get_words()


class BinaryNode:
    def __init__(self, value, count=1):
        self.left = None
        self.right = None
        self.value = value
        self.count = count

    def _insert(self, word, count=1):
        if word == self.value:
            self.count += count
        elif word < self.value:
            if not self.left:
                self.left = BinaryNode(word, count)
            else:
                self.left._insert(word, count)
        else:
            if not self.right:
                self.right = BinaryNode(word, count)
            else:
                self.right._insert(word, count)

    def _search(self, word):
        if self.value == word:
            return self.count
        elif word < self.value:
            if self.left:
                return self.left._search(word)
            else:
                return -1
        else:
            if self.right:
                return self.right._search(word)
            else:
                return -1

    def _get_words(self):
        words = [(self.value, self.count)]
        if self.left:
            words.extend(self.left._get_words())
        if self.right:
            words.extend(self.right._get_words())
        return words
