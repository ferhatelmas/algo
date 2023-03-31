from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l):
            if i < l - 1 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        return [n for n in nums if n] + [n for n in nums if not n]
