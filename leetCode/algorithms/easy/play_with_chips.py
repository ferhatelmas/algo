from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        l = len([chip % 2 for chip in chips])
        return min(l, len(chips) - l)
