class TheAlmostLuckyNumbersDivTwo:
    def find(self, a, b):
        def is_lucky(s):
            return len([e for e in s if e not in "47"]) < 2

        return sum(is_lucky(str(i)) for i in xrange(a, b + 1))
