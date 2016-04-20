import math
import sys


class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        l = math.log(n) / math.log(4)
        return l - int(l) < sys.float_info.epsilon
