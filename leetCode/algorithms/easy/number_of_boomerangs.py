from collections import Counter


class Solution(object):
    def numberOfBoomerangs(self, points):
        s = 0
        for x1, y1 in points:
            c = Counter((x1-x2)**2 + (y1-y2)**2 for x2, y2 in points)
            s += sum(n * (n - 1) for n in c.values())
        return s
