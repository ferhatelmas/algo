class Solution(object):
    def integerReplacement(self, n):
        def s(x, c):
            if x == 1:
                return c
            if x % 2 == 0:
                return s(x / 2, c + 1)
            return min(s(x - 1, c + 1), s(x + 1, c + 1))

        return s(n, 0)
