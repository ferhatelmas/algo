from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(a - b) for a, b in zip(nums, nums[1:] + nums[:1]))
