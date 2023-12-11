from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = set(nums1), set(nums2)
        return [sum(x in b for x in nums1), sum(y in a for y in nums2)]
