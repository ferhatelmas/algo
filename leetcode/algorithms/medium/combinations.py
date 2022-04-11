from itertools import combinations


class Solution:
    def combine(self, n, k):
        return [list(e) for e in combinations(range(1, n + 1), k)]
