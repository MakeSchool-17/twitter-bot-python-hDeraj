import sys
import os
import pickle


def encode(string):
    return "".join(sorted(set(string)))


def createDictionary():
    print("Creating the dictionary...")
    dictionary = {}
    keys = set()
    with open("/usr/share/dict/words", 'r') as f:
        for line in f:
            i = line.strip().lower()
            e = encode(i)
            if e in keys:
                dictionary[e].append(i)
            else:
                dictionary[e] = [i]
                keys.add(e)
    with open("data/edictionary", 'wb') as f:
        pickle.dump(dictionary, f)
    return dictionary


def loadDictionary():
    if "data" not in os.listdir():
        os.mkdir("data")
    if "edictionary" not in os.listdir("data"):
        return createDictionary()
    dictionary = {}
    with open("data/edictionary", 'rb') as f:
        dictionary = pickle.load(f)
    return dictionary


if __name__ == "__main__":
    args = sys.argv[1:]
    dictionary = loadDictionary()
    word = args[0]
    e = encode(word)
    print("Input word: " + word)
    matches = dictionary[e] if e in dictionary.keys() else []
    anagrams = []
    for i in matches:
        if sorted(i) == sorted(word):
            anagrams.append(i)
    if word in anagrams:
        anagrams.remove(word)
    print("Anagrams: " + ", ".join(anagrams))
