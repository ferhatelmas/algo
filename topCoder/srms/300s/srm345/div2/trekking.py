from sys import maxint


class Trekking:
    def findCamps(self, trail, plans):
        c = maxint
        for plan in plans:
            f, d = True, 0
            for t, p in zip(trail, plan):
                if p == "C":
                    d += 1
                    if t == "^":
                        f = False
                        break
            if f:
                c = min(c, d)
        return -1 if c == maxint else c
