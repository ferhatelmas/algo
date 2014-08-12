class Solution:
    def setZeroes(self, matrix):
        rows, cols = set(), set()
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if c == 0:
                    rows.add(i)
                    cols.add(j)

        l = len(matrix[0])
        for r in rows:
            matrix[r] = [0] * l

        for c in cols:
            for r in matrix:
                r[c] = 0


