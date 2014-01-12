class InverseFactoring:
    def getTheNumber(self, factors):
        ls = sorted(factors)
        return ls[0] * ls[-1]
