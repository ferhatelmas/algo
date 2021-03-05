class NoOrderOfOperations:
    def evaluate(self, expr):
        p = int(expr[0])
        for i in xrange(1, len(expr), 2):
            op, r = expr[i], int(expr[i + 1])
            if op == "+":
                p += r
            elif op == "-":
                p -= r
            else:
                p *= r
        return p
