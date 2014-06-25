class BinaryPolynomialDivTwo:
    def countRoots(self, a):
        c = 0
        for x in (0, 1):
            s = 0
            for i, j in enumerate(a):
                if not i:
                    s += j
                else:
                    s += j * x**i
            c += 0 if s%2 else 1
        return c
