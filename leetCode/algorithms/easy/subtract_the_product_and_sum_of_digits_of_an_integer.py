class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        p, t = 1, 0
        for e in s:
            v = int(e)
            p, t = p * v, t + v
        return p - t
