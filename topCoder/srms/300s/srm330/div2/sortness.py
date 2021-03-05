class Sortness:
    def getSortness(self, a):
        s = 0.0
        for i, e in enumerate(a):
            s += len(filter(lambda j: j > e, a[:i]))
            s += len(filter(lambda j: j < e, a[i + 1 :]))
        return s / len(a)
