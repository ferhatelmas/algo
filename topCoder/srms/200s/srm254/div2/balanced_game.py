from math import ceil

class BalancedGame:
    def result(self, conflicts, p, q):
        le = len(conflicts)
        w, l = int(ceil((le-1)*p/100.0)), int(ceil((le-1)*q/100.0))
        for i, c in enumerate(conflicts):
            if c.count('W') < w or c.count('L') < l:
                return i
        return -1
