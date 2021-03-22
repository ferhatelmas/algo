from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m = 0
        for i, e in enumerate(nums):
            curr, prev = e, e
            for j, f in enumerate(nums[i + 1 :]):
                if f > prev:
                    curr, prev = curr + f, f
                else:
                    break
            m = max(m, curr)
        return m
