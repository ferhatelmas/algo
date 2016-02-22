import sys


class Solution:
    def increasingTriplet(self, nums):
        if not nums:
            return False
        a, b = nums[0], sys.maxint
        for e in nums[1:]:
            if e <= a:
                a = e
            elif e < b:
                b = e
            elif e > b:
                return True
        return False
