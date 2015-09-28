from histogram import Histogram
from radixtree import RadixTree
from binarytree import BinaryTree
import timeit
import string
import pickle


rad = RadixTree()
bin = BinaryTree()


def get_full_word_list():
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


def test_inserts(words, tree):
    hist = Histogram(tree)
    for i in words:
        hist.add_word(i)


def test_frequency(word, hist):
    hist.frequency(word)


WORDS_ALL = get_full_word_list()
WORDS_100 = WORDS_ALL[:100]


if __name__ == "__main__":
    radix_freq = Histogram(RadixTree)
    binary_freq = Histogram(BinaryTree)
    for word in WORDS_ALL:
        radix_freq.add_word(word)
        binary_freq.add_word(word)

    print("radix_space: ", len(pickle.dumps(radix_freq)))
    print("binary_space: ", len(pickle.dumps(binary_freq)))

    radix_insert_test = "test_inserts(WORDS_100, RadixTree)"
    binary_insert_test = "test_inserts(WORDS_100, BinaryTree)"
    radix_freq_test = "test_frequency('{}', radix_freq)".format(WORDS_ALL[-1])
    binary_freq_test = "test_frequency('{}',binary_freq)".format(WORDS_ALL[-1])

    trial_nums = [10, 100, 1000, 10000]

    row = ["num", "radix_insert", "binary_insert",
           "radix_freq", "binary_freq"]
    print(row)

    tests = [radix_insert_test,
             binary_insert_test,
             radix_freq_test,
             binary_freq_test]

    for num in trial_nums:
        row = [str(num)]
        for test in tests:
            timer = timeit.Timer(test, globals=globals())
            result = timer.timeit(number=num)
            row.append(result)
        print(row)
