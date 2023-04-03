from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        for i in range(0, 10):
            if i in s1 and i in s2:
                return i
        return int("".join(str(e) for e in sorted([min(nums1), min(nums2)])))
