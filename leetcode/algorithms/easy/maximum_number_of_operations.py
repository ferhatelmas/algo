from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        i, l, s, c = 0, len(nums), 0, 0
        while i < l - 1:
            print(i, s)
            if i == 0:
                s = nums[i] + nums[i + 1]
                c += 1
                i += 2
                continue
            if s == nums[i] + nums[i + 1]:
                c += 1
                i += 2
                continue
            break
        return c
