class WorkingRabbits:
    def getEfficiency(self, profit):
        l = len(profit)
        return sum(int(c)
                   for i, r in enumerate(profit)
                   for c in r[i+1:]) / (((l-1)*l)/2.0)
