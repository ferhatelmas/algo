from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l = len(arr)
        m = min(arr[i] - arr[i - 1] for i in range(1, l))
        return [[arr[i - 1], arr[i]] for i in range(1, l) if arr[i] - arr[i - 1] == m]

