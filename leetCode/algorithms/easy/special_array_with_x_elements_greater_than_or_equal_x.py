from bisect import bisect_left
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        for i in range(0, l + 1):
            j = bisect_left(nums, i)
            if l - j == i:
                return i
        return -1
