import sys
import os


def encode(string):
    s = sorted(string)
    return "".join(s)


def createDictionary():
    f = open("/usr/share/dict/words", 'r')
    b = f.readlines()
    f.close()
    b = [i.split("\n")[0].lower() for i in b]
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
    if "edictionary" not in os.listdir('data'):
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
    print("Loading the dictionary...")
    dictionary = loadDictionary()
    word = args[0]
    e = encode(word)
    print("Input word: " + word)
    anagrams = dictionary[e] if e in dictionary.keys() else ["none"]
    if len(anagrams) == 1 and anagrams[0] == word:
        anagrams = ["none"]
    print("Anagrams: " + ", ".join(anagrams))
