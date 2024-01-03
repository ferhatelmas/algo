from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def isInscreasing(ls):
            p = None
            for i, e in enumerate(ls):
                if i == 0:
                    p = e
                    continue
                if e <= p:
                    return False
                p = e
            return True

        count, l = 0, len(nums)
        for i in range(l):
            for j in range(i + 1, l + 1):
                ls = nums[:i] + nums[j:]
                count += isInscreasing(ls)
        return count
