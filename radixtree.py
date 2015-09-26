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
            progress = False
            for i in current.children:
                if word.find(builder + i.prefix) == 0:
                    current = i
                    builder += i.prefix
                    progress = True
                    break
            if not progress:
                return False
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
                    found = True
                    if common == word:
                        # if it matches rest of word
                        i.frequency += 1
                        return True
                    word = word.replace(common, "")
                    current = i
                    break
                elif common != "":
                    # if it partially matches the prefix
                    found = True
                    if common == word:
                        # complete match, need to split
                        new_node = RadixNode(i.prefix.replace(common, ""), i)
                        new_node.frequency = i.frequency
                        new_node.children = i.children
                        i.prefix = common
                        i.children = [new_node]
                        for j in new_node.children:
                            j.parent = new_node
                        done = True
                    else:
                        new_root = RadixNode(common, current)
                        new_node = RadixNode(
                            word.replace(common, ""),
                            new_root)
                        new_node.frequency = 1
                        i.prefix = i.prefix.replace(common, "")
                        i.parent = new_root
                        new_root.children = [i, new_node]
                        current.children[current.children.index(i)] = new_root
                        done = True
                    break
            if not found:
                new_leaf = RadixNode(word, current)
                new_leaf.frequency = 1
                current.children.append(new_leaf)
                done = True

    def delete(self, word):
        current = self.root
        builder = ""
        while not current.is_leaf() and builder != word:
            for i in current.children:
                if word.find(builder + i.prefix) == 0:
                    current = i
                    builder += i.prefix
                    break
        current.frequency -= 1
        if len(current.children) > 0:
            if current.frequency == 0 and len(current.children) == 1:
                self._squash(current, current.children[0])
        else:
            if current.frequency <= 0:
                current.parent.children.remove(current)
                if len(current.parent.children) == 1:
                    other = current.parent.children[0]
                    self._squash(current.parent, other)
                current.parent = None

    def _squash(self, parent, child):
        parent.prefix += child.prefix
        parent.frequency += child.frequency
        child.parent = None
        parent.children = child.children
        for i in parent.children:
            i.parent = parent
        child.children = None


class RadixNode:
    def __init__(self, prefix="", parent=None):
        self.prefix = prefix
        self.children = []
        self.frequency = 0
        self.parent = parent

    def __str__(self, indent=0):
        val = self.prefix + " (" + str(self.frequency) + ")"
        ret = "\t"*indent + val + "\n"
        if indent == 0:
            ret = "[root]\n"
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
