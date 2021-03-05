class BasketsWithApples:
    def removeExcess(self, apples):
        m, l = 0, len(apples)
        for i, e in enumerate(sorted(apples)):
            m = max(m, e * (l - i))
        return m
