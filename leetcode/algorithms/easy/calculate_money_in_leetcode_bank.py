class Solution:
    def totalMoney(self, n: int) -> int:
        s, m, p, t = 0, 0, 0, 0
        while t < n:
            if t % 7 == 0:
                m += 1
                s += m
                p = m
            else:
                p += 1
                s += p
            t += 1

        return s
