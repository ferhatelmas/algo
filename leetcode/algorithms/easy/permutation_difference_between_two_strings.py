class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {e: i for i, e in enumerate(s)}
        return sum(abs(i - d[e]) for i, e in enumerate(t))
