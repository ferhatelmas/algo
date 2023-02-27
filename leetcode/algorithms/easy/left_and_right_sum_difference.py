from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ls, l, r = [], 0, sum(nums)
        for n in nums:
            r -= n
            ls.append(abs(l - r))
            l += n
        return ls
