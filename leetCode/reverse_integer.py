class Solution:
    def reverse(self, x):
        return -int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
