class LISNumberDivTwo:
    def calculate(self, seq):
        p, c = seq[0], 1
        for e in seq[1:]:
            if e <= p:
                c += 1
            p = e
        return c
