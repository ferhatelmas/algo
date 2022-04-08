from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s, r = sum(nums), 0
        for i, e in enumerate(nums):
            n = s - e
            if r == n:
                return i
            s, r = n, r + e
        return -1
