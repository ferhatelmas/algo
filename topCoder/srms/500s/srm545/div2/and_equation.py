from operator import __and__


class ANDEquation:
    def restoreY(self, A):
        m = max(A)
        for i, e in enumerate(A):
            if e == reduce(__and__, A[:i] + A[i + 1 :], m):
                return e
        return -1
