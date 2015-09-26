class RadixTree:
    def __init__(self, words=[]):
        self.root = RadixNode()
        self.numberOfWords = 0
        if len(words) > 0:
            for word in words:
                self.insert(word)

    def __str__(self):
        return str(self.root)

    def search(self, word):
        current = self.root
        builder = ""
        while not current.is_leaf() and len(builder) < len(word):
            for i in current.children:
                if word.find(builder + i.prefix) == 0:
                    current = i
                    builder += i.prefix
                    break
        return builder == word

    def insert(self, word):
        current = self.root
        done = False
        while not done:
            found = False
            for i in current.children:
                common = common_prefix(word, i.prefix)
                if common == i.prefix:
                    # if it matches the entire prefix
                    if common == word:
                        # if it matches rest of word
                        i.frequency += 1
                        done = True
                    found = True
                    word = word.replace(common, "")
                    current = i
                    break
                elif common != "":
                    # if it partially matches the prefix
                    found = True
                    new_node = RadixNode(word.replace(common, ""))
                    new_node.frequency = 1
                    new_root = RadixNode(common)
                    i.prefix = i.prefix.replace(common, "")
                    new_root.children = [i, new_node]
                    current.children[current.children.index(i)] = new_root
                    done = True
                    pass
            if not found:
                new_leaf = RadixNode(word)
                new_leaf.frequency = 1
                current.children.append(new_leaf)
                done = True

    def delete(self, word):
        pass


class RadixNode:
    def __init__(self, prefix=""):
        self.prefix = prefix
        self.children = []
        self.frequency = 0

    def __str__(self, indent=0):
        val = self.prefix + " (" + str(self.frequency) + ")"
        ret = "\t"*indent + val + "\n"
        for child in self.children:
            ret += child.__str__(indent + 1)
        return ret

    def is_leaf(self):
        return len(self.children) == 0


def common_prefix(a, b):
    prefix = 0
    while b.find(a[:prefix+1]) == 0 and prefix < min(len(a), len(b)):
        prefix += 1
    return a[:prefix]


if __name__ == "__main__":
    print("RadixTree")
