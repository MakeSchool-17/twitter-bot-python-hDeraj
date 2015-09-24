import random
import sys


def loadDictionary():
    f = open("/usr/share/dict/words", 'r')
    b = f.readlines()
    f.close()
    return [i.split("\n")[0] for i in b]


if __name__ == "__main__":
    args = sys.argv[1:]
    print("Loading the dictionary...")
    dictionary = loadDictionary()
    numwords = int(args[0])
    indexes = [random.randint(0, len(dictionary)) for i in range(numwords)]
    print(" ".join([dictionary[i] for i in indexes]))
