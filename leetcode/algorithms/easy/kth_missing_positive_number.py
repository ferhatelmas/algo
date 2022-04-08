from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n, i, l = 1, 0, len(arr)
        while k > 0:
            if i < l:
                if n == arr[i]:
                    i += 1
                else:
                    k -= 1
            else:
                k -= 1
            n += 1
        return max(n - 1, 1)
