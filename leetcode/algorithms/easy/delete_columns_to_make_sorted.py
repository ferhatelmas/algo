from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(list(ls) != sorted(ls) for ls in zip(*A))
