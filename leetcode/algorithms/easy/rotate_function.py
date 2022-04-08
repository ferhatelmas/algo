class Solution(object):
    def maxRotateFunction(self, A):
        if not A:
            return 0
        l, s = len(A), sum(A)
        n = m = sum(a * b for a, b in zip(A, range(l)))
        for e in reversed(A):
            n += s - e * l
            m = max(m, n)
        return m
