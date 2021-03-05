from itertools import groupby


class LinearPolyominoCovering:
    def findCovering(self, region):
        s = []
        for k, g in groupby(region):
            ls = list(g)
            if k == ".":
                s.extend(ls)
            else:
                l = len(ls)
                if l % 2 == 1:
                    return "impossible"
                else:
                    s.append("AAAA" * (l / 4))
                    s.append("BB" if l % 4 else "")
        return "".join(s)
