from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(e % (f * k) == 0 for e in nums1 for f in nums2)
