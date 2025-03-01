from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted(n % 2 for n in nums)
