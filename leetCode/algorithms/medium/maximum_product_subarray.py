class Solution:
    def maxProduct(self, A):
        a = b = r = A[0]
        for x in A[1:]:
            a, b = max(x, a * x, b * x), min(x, a * x, b * x)
            r = max(r, a)
        return r
