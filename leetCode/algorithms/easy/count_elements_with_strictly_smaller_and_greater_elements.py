from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0

        a, b = min(nums), max(nums)
        return sum(a < v < b for v in nums)
