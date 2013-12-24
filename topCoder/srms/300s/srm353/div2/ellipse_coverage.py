class EllipseCoverage:
    def calculateCoverage(self, x1, y1, x2, y2, d):
        [m, n], [p, r], c = sorted([x1, x2]), sorted([y1, y2]), 0
        for i in xrange(m-d, n+d+1):
            for j in xrange(p-d, r+d+1):
                if ((x1-i)**2+(y1-j)**2)**0.5 + ((x2-i)**2+(y2-j)**2)**0.5 < d:
                    c += 1
        return c
