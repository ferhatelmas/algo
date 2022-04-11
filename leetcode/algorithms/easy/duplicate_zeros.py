from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i, l = 0, len(arr)
        while i < l:
            e = arr[i]
            if e == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
