from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        l, m = len(mountain), mountain
        return [i for i in range(1, l - 1) if max(m[i - 1], m[i + 1]) < m[i]]
