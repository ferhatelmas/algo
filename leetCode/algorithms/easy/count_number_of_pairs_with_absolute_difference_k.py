from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return sum(abs(a - b) == k for i, a in enumerate(nums) for b in nums[i + 1 :])
