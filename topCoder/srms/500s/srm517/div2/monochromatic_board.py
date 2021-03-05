class MonochromaticBoard:
    def theMin(self, board):
        rc, cc = len(board), len(board[0])

        def c(t):
            return sum("W" not in r for r in t)

        rs, cs = c(board), c(*board)
        if rs == rc or cc == cs:
            return min(rs, cs)
        return rs + cs
