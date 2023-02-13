from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        s, i, j = 0, 0, len(nums) - 1
        while i <= j:
            if i == j:
                s += nums[i]
                break
            s += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        return s
