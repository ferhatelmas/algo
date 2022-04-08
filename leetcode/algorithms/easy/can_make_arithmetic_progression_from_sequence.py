from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return len(set(a - b for a, b in zip(arr, arr[1:]))) == 1
