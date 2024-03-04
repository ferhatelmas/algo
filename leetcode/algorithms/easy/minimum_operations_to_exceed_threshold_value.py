from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(e < k for e in nums)
