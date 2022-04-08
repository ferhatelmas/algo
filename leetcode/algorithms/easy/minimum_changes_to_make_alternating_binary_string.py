other = {"0": "1", "1": "0"}


class Solution:
    def minOperations(self, s: str) -> int:
        c, d = "0", 0
        for e in s:
            d, c = d + (c != e), other[c]

        c, m, d = "1", d, 0
        for e in s:
            d, c = d + (c != e), other[c]
        return min(m, d)
