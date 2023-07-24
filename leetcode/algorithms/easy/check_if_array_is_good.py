from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        if len(nums) - 1 != nums[-1]:
            return False
        for i, e in enumerate(nums[:-1], start=1):
            if i != e:
                print(i, e)
                return False
        return True
