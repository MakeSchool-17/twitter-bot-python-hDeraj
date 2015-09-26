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
                    if common == word:
                        # complete match, need to split
                        new_node = RadixNode(i.prefix.replace(common, ""), i)
                        new_node.frequency = i.frequency
                        i.prefix = common
                        i.children.append(new_node)
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
        while not current.is_leaf() and len(builder) < len(word):
            for i in current.children:
                if word.find(builder + i.prefix) == 0:
                    current = i
                    builder += i.prefix
                    break
        if len(current.children) > 0:
            current.frequency -= 1
            if current.frequency == 0 and len(current.children) == 1:
                current.prefix += current.children[0].prefix
                current.frequency = current.children[0].frequency
                current.children[0].parent = None
                temp_children = current.children[0].children
                current.children[0].children = []
                current.children = temp_children
                for i in current.children:
                    i.parent = current
        else:
            current.frequency -= 1
            if current.frequency <= 0:
                print(current.parent.prefix)
                print(current.parent.children)
                print(current.prefix)
                current.parent.children.remove(current)
                if len(current.parent.children) == 1:
                    other = current.parent.children[0]
                    current.parent.prefix += other.prefix
                    current.parent.frequency += other.frequency
                    other.parent = None
                    current.parent.children = other.children
                current.parent = None


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


def run_test():
    a = RadixTree()
    words = ["hello", "head", "testing", "tents", "ten", "tent"]
    for word in words:
        a.insert(word)
    return a

if __name__ == "__main__":
    print("RadixTree")
