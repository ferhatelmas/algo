from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for n in range(left, right + 1):
            if not any(a <= n <= b for a, b in ranges):
                return False
        return True
