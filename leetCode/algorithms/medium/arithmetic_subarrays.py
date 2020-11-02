from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        return [self.isArithmetic(sorted(nums[i : j + 1])) for i, j in zip(l, r)]

    def isArithmetic(self, nums: List[int]) -> bool:
        i, l = 1, len(nums) - 1
        if l < 2:
            return True
        diff = nums[0] - nums[i]
        while i < l:
            if diff != nums[i] - nums[i + 1]:
                return False
            i += 1
        return True
