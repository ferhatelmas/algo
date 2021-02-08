from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        ls = sorted(nums)
        return any(nums[i:] + nums[:i] == ls for i in range(len(nums)))
