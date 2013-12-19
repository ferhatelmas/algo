class RugSizes:
    def rugCount(self, area):
        s, c = set(), 0
        for i in xrange(1, area+1):
            if area%i == 0:
                b = area/i
                if b not in s and not(i != b and i%2 == 0 and b%2 == 0):
                    c += 1
                    s.add(i)
        return c
