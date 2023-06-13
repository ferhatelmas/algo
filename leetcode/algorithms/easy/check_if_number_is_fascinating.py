class Solution:
    def isFascinating(self, n: int) -> bool:
        s = sorted(str(n) + str(2 * n) + str(3 * n))
        return s == list("123456789")
