from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        v, c = 0, 0
        for e, n in Counter(s).items():
            if e in "aeiou":
                v = max(v, n)
            else:
                c = max(c, n)
        return v + c
