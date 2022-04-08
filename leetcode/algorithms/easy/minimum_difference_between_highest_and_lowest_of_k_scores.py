from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        m = 100001
        nums.sort()
        for i in range(0, len(nums) - k + 1):
            m = min(m, nums[i + k - 1] - nums[i])
        return m
