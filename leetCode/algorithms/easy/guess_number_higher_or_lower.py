def guess(num: int) -> bool:
    """Provided API"""
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r, g = 1, n, (1 + n) / 2
        v = guess(g)
        while v:
            if v == 1:
                l = g + 1
            else:
                r = g - 1
            g = (l + r) / 2
            v = guess(g)
        return g
