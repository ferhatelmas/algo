class Solution:
    def totalNQueens(self, n):
        self.cols, self.d1, self.d2 = set(), set(), set()
        return self.compute(0, 0, n)

    def compute(self, r, c, n):
        for i in range(n):
            if i in self.cols:
                continue
            d1 = r - i
            if d1 in self.d1:
                continue
            d2 = r + i
            if d2 in self.d2:
                continue
            if r == n - 1:
                c += 1
            else:
                self.cols.add(i)
                self.d1.add(d1)
                self.d2.add(d2)
                c = self.compute(r+1, c, n)
                self.cols.remove(i)
                self.d1.remove(d1)
                self.d2.remove(d2)
        return c
