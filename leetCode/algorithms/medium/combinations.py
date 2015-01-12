class Solution:
    def combine(self, n, k):
        return [list(e) for e in itertools.combinations(range(1, n+1), k)]
