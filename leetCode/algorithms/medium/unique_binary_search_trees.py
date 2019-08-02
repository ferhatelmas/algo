from operator import mul


class Solution:
    def numTrees(self, n):
        return reduce(mul, xrange(2 * n, n, -1), 1) / (
            (n + 1) * reduce(mul, xrange(1, n + 1), 1)
        )
