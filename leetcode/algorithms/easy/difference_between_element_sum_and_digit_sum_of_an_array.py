from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ts, ds = 0, 0
        for n in nums:
            ts += n
            ds += sum(int(e) for e in str(n))
        return abs(ts - ds)
