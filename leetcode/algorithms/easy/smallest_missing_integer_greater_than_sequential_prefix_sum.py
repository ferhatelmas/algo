from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        p, t, s = nums[0], nums[0], set(nums)
        for e in nums[1:]:
            if e == p + 1:
                p = e
                t += p
            else:
                break
        while t in s:
            t += 1
        return t
