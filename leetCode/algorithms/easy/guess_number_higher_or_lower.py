def guess(num):
    """ Provided API"""
    pass


class Solution(object):
    def guessNumber(self, n):
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
