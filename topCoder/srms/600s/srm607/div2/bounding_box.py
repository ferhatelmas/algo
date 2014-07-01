from sys import maxint

class BoundingBox:
    def smallestArea(self, X, Y):
        xa, xb, ya, yb = maxint, -maxint, maxint, -maxint
        for x, y in zip(X, Y):
            xa, xb = min(xa, x), max(xb, x)
            ya, yb = min(ya, y), max(yb, y)
        return (xb-xa) * (yb-ya)
