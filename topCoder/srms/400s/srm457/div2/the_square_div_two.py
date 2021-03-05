class TheSquareDivTwo:
    def solve(self, board):
        r, l = [sum(i == "C" for i in b) for b in board], len(board)
        s = [["."] * l for _ in r]
        for j in xrange(l):
            for i in xrange(l - 1, l - r[j] - 1, -1):
                s[i][j] = "C"
        return ["".join(i) for i in s]
