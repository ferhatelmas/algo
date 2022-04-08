class Solution:
    def canWinNim(self, n):
        return n > 0 and n % 4 != 0
