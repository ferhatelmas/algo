class Solution:

    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        ls = sorted(num)
        return max(b - a for a, b in zip(ls, ls[1:]))
