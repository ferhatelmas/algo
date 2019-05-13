import math


class Solution:
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        diff = int(math.log(n - m) / math.log(2) + 1)
        m >>= diff
        n >>= diff
        return (m & n) << diff


print(Solution().rangeBitwiseAnd(5, 7))
