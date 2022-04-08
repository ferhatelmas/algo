from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        d, m = defaultdict(int), 0
        for i in range(1, n + 1):
            n = sum(int(e) for e in str(i))
            d[n] += 1
            m = max(m, d[n])
        return sum(e == m for e in d.values())
