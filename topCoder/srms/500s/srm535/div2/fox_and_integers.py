class FoxAndIntegers:
    def get(self, AminusB, BminusC, AplusB, BplusC):
        a = (AminusB + AplusB) / 2
        b = AplusB - a
        c = BplusC - b
        if a - b == AminusB and b - c == BminusC:
            return (a, b, c)
        return ()
