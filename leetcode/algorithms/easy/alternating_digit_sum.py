class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s, m = 0, 1
        for e in str(n):
            s += int(e) * m
            m *= -1
        return s
