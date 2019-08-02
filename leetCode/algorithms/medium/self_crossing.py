class Solution:
    def isSelfCrossing(self, x):
        for i, c in enumerate(x[3:], start=3):
            ppp, pp, p = x[i - 3 : i]
            if c >= pp and p <= ppp:
                return True
            elif i >= 4 and p == ppp and c + x[i - 4] >= pp:
                return True
            elif (
                i >= 5
                and pp >= x[i - 4]
                and c + x[i - 4] >= pp
                and p <= ppp
                and p + x[i - 5] >= ppp
            ):
                return True
        return False
