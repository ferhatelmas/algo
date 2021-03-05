class EllysTSP:
    def getMax(self, places):
        c = places.count("C")
        v = len(places) - c
        return 2 * min(c, v) + min(abs(c - v), 1)
