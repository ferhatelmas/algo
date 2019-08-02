import math


class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        return n == 3 ** int(math.log(n, 3) + 0.5)
