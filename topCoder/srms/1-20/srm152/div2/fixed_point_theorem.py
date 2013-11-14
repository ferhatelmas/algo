import sys

class FixedPointTheorem:
    def cycleRange(self, R):
        x, mx, mn = 0.25, -sys.maxint-1, sys.maxint
        for i in xrange(201001):
            x = R * x * (1-x)
            if i > 200000:
                mx = max(mx, x)
                mn = min(mn, x)
        return "%.17f" % (mx-mn)
