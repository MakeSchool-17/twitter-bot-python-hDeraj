import sys
import random


def rearrange(stuff):
    newstuff = stuff[:]
    random.shuffle(newstuff)
    return newstuff


def reverse(stuff):
    return stuff[::-1]


def reverseSentence(sentence):
    return " ".join(sentence.split(" ")[::-1])


if __name__ == "__main__":
    args = sys.argv[1:]
    print("rearranging: " + " ".join(rearrange(args)))
    if len(args) == 1:
        print("reversing: " + reverse(args[0]))
    else:
        print("reversing: " + reverseSentence(" ".join(args)))
