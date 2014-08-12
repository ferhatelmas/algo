from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = 0
        self.d = OrderedDict()

    def get(self, key):
        if key in self.d:
            v = self.d[key]
            del self.d[key]
            self.d[key] = v
            return v
        return -1

    def set(self, key, value):
        if self.get(key) == -1:
            if self.items == self.capacity:
                self.d.popitem(False)
                self.items -= 1
            self.d[key] = value
            self.items += 1
        else:
            del self.d[key]
            self.d[key] = value
