class PointErasingTwo:
    def getMaximum(self, y):
        c, l = 0, len(y)
        for i in xrange(l):
            for j in xrange(i+1, l):
                c = max(c, sum((i < k < j and min(y[i], y[j]) < y[k] < max(y[i], y[j])) for k in xrange(l)))
        return c
