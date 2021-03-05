class ChessboardPattern:
    def makeChessboard(self, rows, columns):
        r, s = [], [".", "X"]
        for _ in xrange(rows):
            r.append("".join([s[j % 2] for j in xrange(columns)]))
            s = s[::-1]
        return r[::-1]
