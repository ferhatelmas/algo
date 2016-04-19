class Solution:
    def integerBreak(self, n):
        return n - 1 if n < 4 else 3 ** ((n-2) / 3) * ((n-2) % 3 + 2)
