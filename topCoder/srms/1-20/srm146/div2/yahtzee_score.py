class YahtzeeScore:
    def maxPoints(self, toss):
       return max(map(lambda i: i*toss.count(i), range(1, 7)))
