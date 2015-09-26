import sys
import os
import pickle
from collections import defaultdict


def encode(string):
    return "".join(sorted(set(string)))


def create_dictionary():
    print("Creating the dictionary...")
    dictionary = defaultdict(list)
    with open("/usr/share/dict/words", 'r') as f:
        for line in f:
            i = line.strip().lower()
            e = encode(i)
            dictionary[e].append(i)
    with open("data/edictionary", 'wb') as f:
        pickle.dump(dictionary, f)
    return dictionary


def load_dictionary():
    if "edictionary" not in os.listdir("data"):
        return create_dictionary()
    dictionary = {}
    with open("data/edictionary", 'rb') as f:
        dictionary = pickle.load(f)
    return dictionary


def get_anagrams(dictionary, word):
    e = encode(word)
    matches = dictionary[e] if e in dictionary else []
    anagrams = [i for i in matches if sorted(i) == sorted(word)]
    if word in anagrams:
        anagrams.remove(word)
    return anagrams

if __name__ == "__main__":
    args = sys.argv[1:]
    dictionary = load_dictionary()
    word = args[0]
    print("Input word: " + word)
    anagrams = get_anagrams(dictionary, word)
    print("Anagrams: " + ", ".join(anagrams))
