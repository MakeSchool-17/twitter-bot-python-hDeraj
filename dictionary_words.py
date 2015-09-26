import random
import sys


def load_dictionary():
    with open("/usr/share/dict/words", 'r') as f:
        return [i.strip() for i in f]


if __name__ == "__main__":
    args = sys.argv[1:]
    dictionary = load_dictionary()
    num_words = int(args[0])
    indexes = [random.randint(0, len(dictionary)) for i in range(num_words)]
    print(" ".join([dictionary[i] for i in indexes]))
