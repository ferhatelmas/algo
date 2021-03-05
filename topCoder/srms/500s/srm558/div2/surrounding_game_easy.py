class SurroundingGameEasy:
    def score(self, cost, benefit, stone):
        rc, cc = len(stone), len(stone[0])

        def is_surrounded(i, j):
            if i and stone[i - 1][j] == ".":
                return False
            if j and stone[i][j - 1] == ".":
                return False
            if i < rc - 1 and stone[i + 1][j] == ".":
                return False
            if j < cc - 1 and stone[i][j + 1] == ".":
                return False
            return True

        s = 0
        for i, r in enumerate(stone):
            for j, c in enumerate(r):
                if c == "." and is_surrounded(i, j):
                    s += int(benefit[i][j])
                elif c == "o":
                    s += int(benefit[i][j]) - int(cost[i][j])
        return s
