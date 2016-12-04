class Solution:
    def arrangeCoins(self, n):
        c = i = 0
        while i < n:
            i += 1
            c += i
            n -= i
        return i
