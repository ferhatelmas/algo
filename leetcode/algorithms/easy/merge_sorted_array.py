class Solution:
    def merge(self, A, m, B, n):
        sm, sn, i = m - 1, n - 1, m + n - 1

        while sm >= 0 and sn >= 0:
            if A[sm] > B[sn]:
                A[i] = A[sm]
                sm -= 1
            else:
                A[i] = B[sn]
                sn -= 1
            i -= 1
        while sn >= 0:
            A[i] = B[sn]
            i -= 1
            sn -= 1
