from math import log

class MassiveNumbers:
    def getLargest(self, numberA, numberB):
        a, b = map(int, numberA.split('^'))
        c, d = map(int, numberB.split('^'))
        if b * log(a) > d * log(c):
            return numberA
        return numberB
