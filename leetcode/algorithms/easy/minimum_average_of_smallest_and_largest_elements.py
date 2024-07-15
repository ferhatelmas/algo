from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        m, l = nums[-1] + nums[-2], len(nums) / 2
        for i, e in enumerate(nums):
            if i < l:
                m = min(m, e + nums[-i - 1])
        return m / 2
