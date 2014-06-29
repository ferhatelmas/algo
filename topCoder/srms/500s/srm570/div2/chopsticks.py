from collections import Counter

class Chopsticks:
    def getmax(self, length):
        return sum(v/2 for v in Counter(length).values())
