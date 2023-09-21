from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        # find min and index
        m, idx = -1, -1
        for i, e in enumerate(nums):
            if e < m or m == -1:
                m = e
                idx = i
        # if none, early exit
        if idx == -1:
            return -1
        # apply right shits
        nums = nums[idx:] + nums[:idx]
        # confirm is sorted
        m = -1
        for i, e in enumerate(nums):
            if e <= m:
                return -1
            m = e
        # if correct, return # of shifts
        return len(nums) - idx if idx else 0
