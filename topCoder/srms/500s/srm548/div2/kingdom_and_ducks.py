from collections import Counter

class KingdomAndDucks:
    def minDucks(self, duckTypes):
        c = Counter(duckTypes)
        return max(c.values()) * len(c)
