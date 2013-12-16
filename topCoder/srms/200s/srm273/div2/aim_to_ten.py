class AimToTen:
    def need(self, marks):
        s, l, c = sum(marks), len(marks), 0
        while s < 9.5 * (l + c):
            s += 10
            c += 1
        return c
