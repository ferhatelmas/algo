from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        m, length = -1, len(nums)
        for k in range(l, r + 1):
            for i in range(length - k + 1):
                n = sum(nums[i : i + k])
                if n > 0 and (m == -1 or n < m):
                    m = n
        return m
