class Taxi:
    def maxDis(self, maxX, maxY, taxiDis):
        m = -1.0
        for i in xrange(maxX + 1):
            y = taxiDis - i
            if 0 <= y <= maxY:
                m = max(m, (i ** 2 + y ** 2) ** 0.5)
        return m
