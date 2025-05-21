class Solution:
    def maxProduct(self, n: int) -> int:
        ls = sorted((int(e) for e in str(n)), reverse=True)
        return ls[0] * ls[1]
