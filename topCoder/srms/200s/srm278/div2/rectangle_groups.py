from operator import itemgetter


class RectangleGroups:
    def maximalIndexed(self, rectangles):
        d = {}
        for r in rectangles:
            g, w, l = r.split()
            d[g] = d.get(g, 0) - int(w) * int(l)
        n = sorted(d.items(), key=itemgetter(1, 0))[0]
        return "{} {}".format(n[0], -n[1])
