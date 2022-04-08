class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        ls = [[1]]
        for _ in xrange(numRows - 1):
            el = [1]
            el.extend([a + b for a, b in zip(ls[-1], ls[-1][1:])])
            el.append(1)
            ls.append(el)
        return ls

    def getRow(self, rowIndex):
        return self.generate(rowIndex + 1)[-1]
