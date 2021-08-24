from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        for i in range(a, 1, -1):
            if b % i == 0 and a % i == 0:
                return i
        return 1
