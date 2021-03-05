class Prank:
    def realWeight(self, apparentGain):
        r = []
        for i in xrange(1, 50001):
            s = i ** 2 + apparentGain
            m = int(s ** 0.5)
            if m ** 2 == s:
                print m
                r.append(m)
        return r
