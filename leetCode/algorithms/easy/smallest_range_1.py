from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        a, b = max(A), min(A)
        return max(a - b - 2 * K, 0)
