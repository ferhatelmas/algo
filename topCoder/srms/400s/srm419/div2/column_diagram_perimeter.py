class ColumnDiagramPerimeter:
    def getPerimiter(self, a):
        l = len(a)
        return sum(abs(a[i]-a[i-1]) for i in xrange(1, l)) + 2*l + a[0] + a[-1]
