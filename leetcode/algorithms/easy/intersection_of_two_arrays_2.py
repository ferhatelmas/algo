from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        return [k for k, v in (c1 & c2).items() for _ in range(v)]
