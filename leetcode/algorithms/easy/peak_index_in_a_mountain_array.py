from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i, e in enumerate(A):
            if e > A[i + 1]:
                return i
        return -1
