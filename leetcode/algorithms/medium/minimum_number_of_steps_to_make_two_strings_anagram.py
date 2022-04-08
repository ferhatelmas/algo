from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        return sum(max(v - c2.get(k, 0), 0) for k, v in c1.items())
