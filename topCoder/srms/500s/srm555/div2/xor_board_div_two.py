class XorBoardDivTwo:
    def theMax(self, board):
        rc, cc = len(board), len(board[0])

        def mklist():
            return [list(r) for r in board]

        def flip(ls, i, j):
            for k in xrange(cc):
                ls[i][k] = "0" if ls[i][k] == "1" else "1"
            for k in xrange(rc):
                ls[k][j] = "0" if ls[k][j] == "1" else "1"
            return ls

        def ssum(ls):
            return sum(r.count("1") for r in ls)

        return max(ssum(flip(mklist(), i, j)) for i in xrange(rc) for j in xrange(cc))
