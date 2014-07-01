class CostOfDancing:
    def minimum(self, K, danceCost):
        return sum(sorted(danceCost)[:K])
