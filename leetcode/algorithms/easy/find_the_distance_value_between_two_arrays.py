from bisect import bisect_right
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        a, cnt, l = sorted(arr2), 0, len(arr2)
        for e in arr1:
            n = bisect_right(a, e)
            if n > -1 and abs(e - a[n - 1]) <= d:
                continue
            if n < l and abs(e - a[n]) <= d:
                continue
            cnt += 1
        return cnt
