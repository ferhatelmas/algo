from string import digits


class Solution:
    def minMaxDifference(self, num: int) -> int:
        ma, mi, s = -1, 10**8, str(num)
        for a in digits:
            for b in digits:
                n = int("".join(b if e == a else e for e in s))
                ma = max(ma, n)
                mi = min(mi, n)
        return ma - mi


Solution().minMaxDifference(11891)
