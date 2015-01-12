class Solution:

    def trailingZeroes(self, n):
        c = 0
        while n >= 5:
            n /= 5
            c += n
        return c
