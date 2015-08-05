class Solution:
    def generateMatrix(self, n):
        res, l = [], n * n + 1
        while l > 1:
            l, h = l - len(res), l
            res = [range(l, h)] + zip(*res[::-1])
        return res
