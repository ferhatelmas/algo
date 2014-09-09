class InterestingDigits:
    def digits(self, base):
        return [i for i in xrange(2, base) if base%i == 1]
