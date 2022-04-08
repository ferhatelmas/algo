from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = -1
        for i, a in enumerate(nums):
            for b in nums[i + 1 :]:
                if b > a:
                    m = max(m, b - a)
        return m
