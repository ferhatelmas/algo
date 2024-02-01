from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i] + nums[-i - 1] for i in range(len(nums) // 2))
