from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s, l = 0, len(arr)
        for i in range(1, l + 1, 2):
            for j in range(0, l - i + 1):
                s += sum(arr[j : j + i])
        return s
