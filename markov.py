"""
A Markov model for text generation

@hDeraj 2015
"""
import random
import string

class Markov:
    def __init__(self, words):
        self.words = words[:]
        self.table = {}
        for i in range(len(words) - 1):
            for j in range(2):
                if i-j >= 0:
                    self._make_link(" ".join(words[i-j:i]), words[i+1])

    def _make_link(self, a, b):
        ha = hash(a)
        hb = hash(b)
        if hb not in self.table:
            self.table[hb] = MarkovNode(b)
        if ha not in self.table:
            self.table[ha] = MarkovNode(a)
        self.table[ha].add_state(b, hb)

    def predict(self, word):
        h = hash(word)
        if h not in self.table:
            return None
        return self.table[h].predict()


class MarkovNode:
    def __init__(self, state):
        self.state = state
        self.new_states = []
        self.entries = 0

    def add_state(self, new_state, new_hashed_state):
        self.entries += 1
        for state in self.new_states:
            if state[0] == new_state:
                state[1] += 1
        else:
            self.new_states.append([new_state, 1, new_hashed_state])

    def predict(self):
        r = random.randrange(0, self.entries)
        c = 0
        i = 0
        while c <= r:
            c += self.new_states[i][1]
            i += 1
        return self.new_states[i][0]


def get_full_word_list():
    bad = string.punctuation + "-\n"
    table = str.maketrans(bad, " "*len(bad))
    words = []
    with open("data/corpus.txt", 'r') as f:
        for i in f:
            if i == "\n":
                continue
            words.extend(i.translate(table).strip().lower().split(" "))
    words = [i for i in words if i.strip() != ""]
    return words

def new_markov_test():
    words = get_full_word_list()
    return Markov(words)



if __name__ == "__main__":
    print("Markov")
