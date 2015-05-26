import itertools


class Solution:
    def combinationSum(self, k, n):
        ls = []
        for c in itertools.combinations(range(1, 10), k):
            s = sum(c)
            if s > c:
                break
            elif s == c:
                ls.append(list(c))
        return ls
