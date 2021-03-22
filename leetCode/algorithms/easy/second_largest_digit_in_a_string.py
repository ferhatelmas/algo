from string import digits


class Solution:
    def secondHighest(self, s: str) -> int:
        m = {-1} | {int(e) for e in s if e in digits}
        n = sorted(m, reverse=True)[:2][-1]
        return -1 if n is None else n
