from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        d = None
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if d is None:
                d = diff
            elif diff > d:
                return arr[i] + diff // 2
            elif diff < d:
                return arr[i] - diff
        return arr[0]
