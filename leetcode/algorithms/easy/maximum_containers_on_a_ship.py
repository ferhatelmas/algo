class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        k = maxWeight // w
        m = n * n
        return k if k < m else m
