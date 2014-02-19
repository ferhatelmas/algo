class MatrixShiftings:
    def minimumShifts(self, matrix, value):
        lr, lc = len(matrix), len(matrix[0])
        m = lr + lc
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if int(c) == value:
                    m = min(min(i, lr-i) + min(j, lc-j), m)
        return -1 if lr + lc == m else m
