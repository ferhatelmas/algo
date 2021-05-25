from itertools import groupby


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero, one = 0, 0
        for k, g in groupby(s):
            l = len(list(g))
            if k == "0":
                zero = max(zero, l)
            else:
                one = max(one, l)
        return one > zero
