from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cnt, prev = 0, 0
        for a, b in sorted(nums):
            cnt += max(b - max(a, prev) + (a > prev), 0)
            prev = max(prev, b)
        return cnt
