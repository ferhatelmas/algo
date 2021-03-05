import re
from collections import Counter


class KingXNewBaby:
    def isValid(self, name):
        if len(name) != 8 or re.search("[^a-z]", name):
            return "NO"
        c, s = Counter(name), 0
        for e in "aeiou":
            s += c[e]
            if c[e] == 1:
                return "NO"
        return "YES" if s == 2 else "NO"
