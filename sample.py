from histogram import Histogram
import sys
import os
import random


class SamplerHistogram(Histogram):
    def sample(self):
        words = self._tree.get_words()
        if len(words) == 0:
            return None
        choice = random.randint(1, self.entries())
        cur = 0
        prob = words[0][1]
        while prob < choice:
            cur += 1
            prob += words[cur][1]
        return words[cur][0]


if __name__ == "__main__":
    args = sys.argv[1:]
    hist = SamplerHistogram()
    if len(args) == 0:
        print("no arguments given")
    elif len(args) == 1:
        if os.path.isfile(args[0]):
            hist.load_from_file(args[0])
        else:
            print("file doesn't exist")
    else:
        hist.load_from_list(args)

    entries = hist._tree.get_words()
    for i in entries:
        print(i)
