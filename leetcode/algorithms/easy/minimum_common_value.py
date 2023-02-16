from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, il, jl = 0, 0, len(nums1), len(nums2)
        while i < il and j < jl:
            a, b = nums1[i], nums2[j]
            if a == b:
                return a
            if a > b:
                j += 1
            else:
                i += 1
        return -1
