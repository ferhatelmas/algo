class BettingStrategy:
    def finalSum(self, initSum, outcome):
        b, m = 1, initSum
        for e in outcome:
            if e == "W":
                m += b
                b = 1
            else:
                m -= b
                b *= 2
                if m < b:
                    break
        return m
