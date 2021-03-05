class TheBoredomDivTwo:
    def find(self, n, m, j, b):
        c = 0
        if j > n:
            c += 1
        if b > n:
            c += b != j
        return n + c
