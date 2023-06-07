from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        s, l = 0, len(nums)
        for i, e in enumerate(nums):
            if e == 1:
                s += i
            elif e == l:
                if s == 0 and nums[0] != 1:
                    s -= 1
                s += l - i - 1
        return s
