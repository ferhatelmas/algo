class Party:
    def averageNames(self, n, personA, personB):
        ns = [set() for _ in xrange(n)]
        for i, j in zip(personA, personB):
            ns[i] |= ns[j]
            ns[j] |= ns[i]
            ns[i].add(j)
            ns[j].add(i)
        return sum(map(lambda (i, s): len(s) - (i in s), enumerate(ns))) / float(n)
