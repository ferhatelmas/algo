from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = len(arr)
        n = int(l * 0.05)
        return sum(arr[n : l - n]) / (l - 2 * n)
