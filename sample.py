import histogram
import sys
import os
import random


class SamplerHistogram(histogram.Histogram):
    def sample(self):
        keys = list(self.histogram.keys())
        if len(keys) == 0:
            return None
        choice = random.randint(0, self.items)
        cur = 0
        prob = self.histogram[keys[cur]]
        while prob < choice:
            cur += 1
            prob += self.histogram[keys[cur]]
        return keys[cur]


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
