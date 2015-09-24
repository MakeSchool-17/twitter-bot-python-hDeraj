import sys
import os


def encode(string):
    return "".join(sorted(set(string)))


def createDictionary():
    print("Creating the dictionary...")
    f = open("/usr/share/dict/words", 'r')
    b = f.readlines()
    f.close()
    b = sorted([i.split("\n")[0].lower() for i in b])
    dictionary = {}
    for i in b:
        e = encode(i)
        if e in dictionary.keys():
            dictionary[e].append(i)
        else:
            dictionary[e] = [i]
    f = open("data/edictionary", 'w')
    for i in dictionary.keys():
        f.write(i+":"+",".join(dictionary[i])+"\n")
    f.close()


def loadDictionary():
    if "data" not in os.listdir():
        os.mkdir("data")
    if "edictionary" not in os.listdir("data"):
        createDictionary()
    f = open("data/edictionary", 'r')
    lines = f.readlines()
    f.close()
    dictionary = {}
    for i in lines:
        s = i.split("\n")[0].split(":")
        dictionary[s[0]] = s[1].split(",")
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
        if "".join(sorted(i)) == "".join(sorted(word)):
            anagrams.append(i)
    if word in anagrams:
        anagrams.remove(word)
    print("Anagrams: " + ", ".join(anagrams))
