class UniqueDigits:
    def count(self, n):
        def is_different(i):
            return len(set(str(i))) == len(str(i))
        return sum(map(is_different, xrange(1, n)))
