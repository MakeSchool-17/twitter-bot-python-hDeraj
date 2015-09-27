from radixtree import RadixTree


def create_tree(words):
    a = RadixTree()
    for i in words:
        a.insert(i)
    return a


def run_tests():
    words = ["hello", "test", "head", "ten", "testing", "tens"]
    a = create_tree(words)
    assert(a.search("hello") == 1)
    assert(a.search("ten") == 1)
    assert(a.search("tena") == -1)

    a.insert("ten")
    a.delete("tens")

    assert(a.search("ten") == 2)
    assert(a.search("tens") == -1)

    a.delete("ten")

    assert(a.search("ten") == 1)
    print("all tests passed")

if __name__ == "__main__":
    run_tests()
