from math import gcd, lcm
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result, ln = 1, len(nums)
        for i in range(ln):
            p = g = l = nums[i]
            for j, n in enumerate(nums[i + 1 :], start=i + 1):
                p *= n
                g = gcd(g, n)
                l = lcm(l, n)
                if p == (g * l):
                    result = max(result, j - i + 1)

        return result
