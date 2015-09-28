class RadixTree:
    def __init__(self, words=[]):
        """Creates a new RadixTree, and fills it with the supplied words"""
        self.root = RadixNode()
        self.count = 0
        if len(words) > 0:
            for word in words:
                self.insert(word)

    def __str__(self):
        """Returns the formatted tree as a string."""
        return str(self.root)

    def get_words(self):
        """Returns a list of all the words stored in the tree."""
        return self.root._get_words()

    def search(self, word):
        """Returns the frequency of the supplied word in the tree, or -1."""
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
                return -1
        return current.frequency if builder == word else -1

    def insert(self, word, count=1):
        """Inserts the supplied word into the tree."""
        self.count += count
        current = self.root
        while current:
            found = False
            for i in current.children:
                common = common_prefix(word, i.prefix)
                if common == i.prefix:
                    # if it matches the entire prefix
                    found = True
                    if common == word:
                        # if it matches rest of word
                        i.frequency += count
                        return True
                    word = word.replace(common, "", 1)
                    current = i
                    break
                elif common != "":
                    # if it partially matches the prefix
                    found = True
                    if common == word:
                        # complete match, need to split
                        new_node = i._split(common)
                        i.frequency = count
                        return True
                    else:
                        # partial match, split and create neighbor
                        i._split(common)
                        new_prefix = word.replace(common, "", 1)
                        new_node = RadixNode(new_prefix, i)
                        new_node.frequency = count
                        i.children.append(new_node)
                        return True
                    break
            if not found:
                new_leaf = RadixNode(word, current)
                new_leaf.frequency = 1
                current.children.append(new_leaf)
                return True

    def delete(self, word, count=1):
        """Removes the supplied word from the tree."""
        current = self.root
        builder = ""
        while not current.is_leaf() and builder != word:
            for i in current.children:
                if word.find(builder + i.prefix) == 0:
                    current = i
                    builder += i.prefix
                    break
        self.count -= max(0, current.frequency - count)
        current.frequency -= count
        if len(current.children) > 0:
            if current.frequency == 0 and len(current.children) == 1:
                current._squash(current.children[0])
        else:
            if current.frequency <= 0:
                current.parent.children.remove(current)
                if len(current.parent.children) == 1:
                    other = current.parent.children[0]
                    current.parent._squash(other)
                current.parent = None


class RadixNode:
    def __init__(self, prefix="", parent=None):
        """Creates a new RadixNode with the supplied prefix and parent."""
        self.prefix = prefix
        self.children = []
        self.frequency = 0
        self.parent = parent

    def __str__(self, indent=0):
        """
        Displays the prefix and frequency.

        Indents the string according to its depth in the tree.
        """
        val = self.prefix + " (" + str(self.frequency) + ")"
        ret = "\t"*indent + val + "\n"
        if indent == 0:
            ret = "[root] " + ret + "\n"
        for child in self.children:
            ret += child.__str__(indent + 1)
        return ret

    def is_leaf(self):
        """Check if the node has any children."""
        return len(self.children) == 0

    def _squash(self, child):
        """
        Squashes the current node with the supplied child node.


        """
        self.prefix += child.prefix
        self.frequency += child.frequency
        child.parent = None
        self.children = child.children
        for i in self.children:
            i.parent = self
        child.children = None

    def _split(self, prefix):
        """Split the node into a parent and child node."""
        child_prefix = self.prefix.replace(prefix, "", 1)
        child = RadixNode(child_prefix, self)
        self.prefix = prefix
        child.children = self.children
        child.frequency = self.frequency
        self.frequency = 0
        for i in child.children:
            i.parent = child
        self.children = [child]
        return child

    def _get_words(self, prefix=""):
        """
        Returns the words stored in the current node, as well as it's children.

        RECURSION:
        - Recurses to the depth of the tree.
        - Bounded by the length of the biggest word stored.
        """
        words = []
        new_prefix = prefix + self.prefix
        if self.frequency > 0:
            words.append((new_prefix, self.frequency))
        for i in self.children:
            words.extend(i._get_words(new_prefix))
        return words


def common_prefix(a, b):
    """Returns the largest common prefix between the two supplied strings."""
    prefix = 0
    while b.find(a[:prefix+1]) == 0 and prefix < min(len(a), len(b)):
        prefix += 1
    return a[:prefix]


if __name__ == "__main__":
    print("RadixTree")
