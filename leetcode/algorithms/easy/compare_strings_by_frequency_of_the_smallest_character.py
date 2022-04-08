from typing import List


class Solution:
    def small(self, s: str) -> int:
        return s.count(min(list(s)))

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        counts = [self.small(w) for w in words]
        res = []
        for q in queries:
            n = self.small(q)
            res.append(sum(c > n for c in counts))
        return res
