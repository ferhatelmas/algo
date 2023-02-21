from operator import itemgetter
from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        d = {a: b for a, b in nums1}
        for a, b in nums2:
            d[a] = d.get(a, 0) + b
        return [[a, b] for a, b in sorted(d.items(), key=itemgetter(0))]
