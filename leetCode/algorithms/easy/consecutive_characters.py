from itertools import groupby


class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(ls)) for _, ls in groupby(s))
