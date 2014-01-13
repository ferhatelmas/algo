class MegaCoolNumbersEasy:
    def count(self, N):
        def is_mega(s):
            return len(set(ord(s[i]) - ord(s[i-1]) for i in range(1, len(s)))) < 2
        return sum([is_mega(str(e)) for e in xrange(1, N+1)])
