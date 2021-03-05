from math import ceil


class Towers:
    def attack(self, myUnits, hpT, attackT, numT):
        n, r = hpT * numT, 0
        while n > 0 and myUnits > 0:
            r += 1
            n -= myUnits
            myUnits -= attackT * int(ceil(float(n) / hpT))
        return r if myUnits > 0 else -1
