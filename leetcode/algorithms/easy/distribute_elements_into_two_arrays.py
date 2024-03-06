from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        r1, r2 = [], []
        for i, e in enumerate(nums):
            if i == 0:
                r1.append(e)
            elif i == 1:
                r2.append(e)
            else:
                if r1[-1] > r2[-1]:
                    r1.append(e)
                else:
                    r2.append(e)
        return r1 + r2
