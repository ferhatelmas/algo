class GreatFairyWar:
    def minHP(self, dps, hp):
        d, res = sum(dps), 0
        for i, j in zip(hp, dps):
            res += d * i
            d -= j
        return res
