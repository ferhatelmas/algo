from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c, p = 0, -1
        for i, n in enumerate(nums):
            if i == 0:
                p = n
                continue

            diff = n - p
            if diff <= 0:
                c += -diff + 1
                p = n - diff + 1
            else:
                p = n
        return c
