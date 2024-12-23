from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(
            2 * (nums[i] + nums[i + 2]) == nums[i + 1] for i in range(0, len(nums) - 2)
        )
