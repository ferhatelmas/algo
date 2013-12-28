from itertools import product

class SquareDigitNumbers:
    def getNumber(self, n):
        i = 1
        while True:
            for e in product('0149', repeat=i):
                if i > 1 and e[0] == '0':
                    continue
                n -= 1
                if n == -1:
                    return int(''.join(e))
            i += 1
        return 0
