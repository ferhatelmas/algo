class BunnyPuzzle:
    def theCount(self, bunnies):
        c = 0
        for i in bunnies:
            for j in bunnies:
                if i != j:
                    m, n = sorted([i, 2 * j - i])
                    c += not sum(m <= b <= n for b in bunnies if b != i and b != j)
        return c
