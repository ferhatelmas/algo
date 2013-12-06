class YahtzeeScore:
    def maxPoints(self, toss):
        return max(map(lambda i: toss.count(i) * i, xrange(1, 7)))
