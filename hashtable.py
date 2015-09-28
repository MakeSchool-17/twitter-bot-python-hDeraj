from linkedlist import LinkedList


class HashTable:
    def __init__(self, num_bins):
        self.num_bins = num_bins
        self.bins = [HashTableList() for i in range(num_bins)]

    def get(self, key):
        hashed = hash(key) % self.num_bins
        return self.bins[hashed].get(key)

    def set(self, key, value):
        hashed = hash(key) % self.num_bins
        self.bins[hashed].append((key, value))

    def keys(self):
        key_list = []
        for bin in self.bins:
            key_list.extend([key for key, _ in bin.get_all_data()])
        return key_list

    def values(self):
        values_list = []
        for bin in self.bins:
            values_list.extend([value for _, value in bin.get_all_data()])
        return values_list

    def update(self, key, value):
        self.set(key, value)

    def __str__(self):
        s = ""
        c = 0
        for bin in self.bins:
            s += "[" + str(c) + "] : " + bin.__str__() + "\n"
            c += 1
        return s


class HashTableList(LinkedList):
    def get(self, key):
        lookup_func = lambda a: a[0] == key
        return self.find(lookup_func)[1]

    def get_all_data(self):
        data = []
        current = self.head
        while current:
            data.append(current.data)
            current = current.next
        return data

    def __str__(self):
        s = ""
        current = self.head
        while current:
            s += str(current.data)
            if current.next:
                s += " -> "
            current = current.next
        return s
