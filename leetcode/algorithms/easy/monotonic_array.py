from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i, e in enumerate(nums):
            if i == 0:
                continue
            if e > nums[i - 1]:
                decreasing = False
            elif e < nums[i - 1]:
                increasing = False
        return increasing or decreasing
