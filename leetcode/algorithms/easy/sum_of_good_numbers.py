from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        s, l = 0, len(nums)
        for i, e in enumerate(nums):
            a, b = i - k, i + k
            if (a < 0 or e > nums[a]) and (b >= l or e > nums[b]):
                s += e
        return s
