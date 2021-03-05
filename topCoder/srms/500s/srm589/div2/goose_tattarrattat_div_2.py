from collections import Counter


class GooseTattarrattatDiv2:
    def getmin(self, S):
        c = Counter(S)
        return sum(c.values()) - max(c.values())
