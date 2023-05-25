from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        s = 0
        while nums and nums[0]:
            ss = 0
            for i, r in enumerate(nums):
                m = max(r)
                for e in r:
                    if e == m:
                        r.remove(e)
                        break
                ss = max(ss, m)
            s += ss
        return s
