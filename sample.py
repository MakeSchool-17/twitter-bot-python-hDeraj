import histogram
import sys
import os
import random


class SamplerHistogram(histogram.Histogram):
    def sample(self):
        if len(self.histogram.keys()) == 0:
            return None
        return random.choice(list(self.histogram.keys()))


if __name__ == "__main__":
    args = sys.argv[1:]
    hist = SamplerHistogram()
    if len(args) == 0:
        print("no arguments given")
    elif len(args) == 1:
        if args[0] in os.listdir():
            hist.loadFromFile(args[0])
        else:
            print("file doesn't exist")
    else:
        hist.loadFromList(args)
    print(hist.sample())
