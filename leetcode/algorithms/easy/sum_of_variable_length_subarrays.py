from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        t = 0
        for i, e in enumerate(nums):
            t += sum(nums[max(0, i - e) : i + 1])
        return t
