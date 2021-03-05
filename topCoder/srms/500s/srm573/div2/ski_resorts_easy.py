class SkiResortsEasy:
    def minCost(self, altitude):
        s, c = 0, altitude[0]
        for e in altitude:
            if c < e:
                s += e - c
            else:
                c = e
        return s
