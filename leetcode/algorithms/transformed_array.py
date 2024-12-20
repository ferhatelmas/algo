from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        return [nums[(i + num) % l] for i, num in enumerate(nums)]
