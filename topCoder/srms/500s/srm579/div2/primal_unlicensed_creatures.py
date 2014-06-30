class PrimalUnlicensedCreatures:
    def maxWins(self, initialLevel, grezPower):
        c = 0
        for g in sorted(grezPower):
            if g < initialLevel:
                c += 1
                initialLevel += g/2
            else:
                break
        return c
