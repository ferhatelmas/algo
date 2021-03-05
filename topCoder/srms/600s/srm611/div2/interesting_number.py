class InterestingNumber:
    def isInteresting(self, x):
        def cons(i):
            return x[x.index(str(i)) + 1 :].index(str(i)) == i

        for i in xrange(10):
            c = x.count(str(i))
            if c == 0 or (c == 2 and cons(i)):
                continue
            return "Not interesting"
        return "Interesting"
