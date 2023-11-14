from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s, l = 0, len(nums)
        for i in range(1, l + 1):
            for j in range(0, l - i + 1):
                n = len(set(nums[j : j + i]))
                s += n * n
        return s
