from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        l = len(nums)
        mid = l // 2
        i, j, n = 0, mid, 0
        nums.sort()
        while i < mid and j < l:
            if 2 * nums[i] <= nums[j]:
                i += 1
                n += 2
            j += 1
        return n
