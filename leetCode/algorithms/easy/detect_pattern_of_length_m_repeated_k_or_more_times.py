from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(0, len(arr) - m + 1):
            c, base = 1, arr[i : i + m]
            for j in range(1, k):
                if base == arr[i + m + (j - 1) * m : i + m + m * j]:
                    c += 1
                else:
                    break
            if c == k:
                return True
        return False
