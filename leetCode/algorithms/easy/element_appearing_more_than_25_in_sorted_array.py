from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        q = len(arr) // 4
        for i, e in enumerate(arr):
            if (i == 0 or arr[i - 1] != e) and e == arr[i + q]:
                return e
