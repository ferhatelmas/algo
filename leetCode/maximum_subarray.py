class Solution:
    def maxSubArray(self, A):
        e = c = A[0]
        for x in A[1:]:
            e = max(x, e + x)
            c = max(c, e)
        return c
