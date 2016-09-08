from collections import Counter


class Solution(object):
    def canConstruct(self, note, magazine):
        c = Counter(magazine)
        c.subtract(Counter(note))
        return not c or min(c.values()) >= 0
