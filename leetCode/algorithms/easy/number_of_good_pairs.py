from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(a == b for i, a in enumerate(nums) for b in nums[i + 1 :])
