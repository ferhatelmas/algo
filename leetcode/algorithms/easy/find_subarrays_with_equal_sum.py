from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        l = len(nums)
        s = set()
        for i in range(l - 1):
            n = nums[i] + nums[i + 1]
            if n in s:
                return True
            s.add(n)
        return False
