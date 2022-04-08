from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l = len(piles) / 3
        return sum(e for i, e in enumerate(sorted(piles)) if i >= l and i % 2 == l % 2)
