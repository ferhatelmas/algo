from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls, c = [], 0
        for e in nums:
            c += e
            ls.append(c)
        return ls
