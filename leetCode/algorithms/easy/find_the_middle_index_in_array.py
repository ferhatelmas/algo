from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s, far = sum(nums), 0
        for i, v in enumerate(nums):
            if s - v == 2 * far:
                return i
            far += v
        return -1
