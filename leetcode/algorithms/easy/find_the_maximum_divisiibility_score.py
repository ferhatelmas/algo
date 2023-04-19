from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        m, md = -1, -1
        for d in divisors:
            n = sum(n % d == 0 for n in nums)
            if n > m:
                m, md = n, d
            elif n == m:
                md = min(md, d)
        return md
