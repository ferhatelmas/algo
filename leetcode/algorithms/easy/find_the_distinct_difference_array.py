from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        return [len(set(nums[:i])) - len(set(nums[i + 1 :])) for i in enumerate(nums)]
