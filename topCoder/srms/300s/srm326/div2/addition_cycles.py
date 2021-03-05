class AdditionCycles:
    def cycleLength(self, n):
        def cycle(a):
            return (a % 10) * 10 + (a / 10 + a % 10) % 10

        i, m = 1, cycle(n)
        while m != n:
            i += 1
            m = cycle(m)
        return i
