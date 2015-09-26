import sys
import random


def rearrange(stuff):
    new_stuff = stuff[:]
    random.shuffle(new_stuff)
    return new_stuff


def reverse(stuff):
    return stuff[::-1]


def reverse_sentence(sentence):
    return " ".join(sentence.split(" ")[::-1])


if __name__ == "__main__":
    args = sys.argv[1:]
    print("rearranging: " + " ".join(rearrange(args)))
    if len(args) == 1:
        print("reversing: " + reverse(args[0]))
    else:
        print("reversing: " + reverse_sentence(" ".join(args)))
