from functools import reduce
from operator import mul


class Solution:
    def numTrees(self, n):
        return reduce(mul, range(2 * n, n, -1), 1) / (
            (n + 1) * reduce(mul, range(1, n + 1), 1)
        )
