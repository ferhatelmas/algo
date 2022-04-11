from functools import reduce


class Solution:
    def singleNumber(self, A):
        return reduce(lambda a, b: a ^ b, A, 0)
