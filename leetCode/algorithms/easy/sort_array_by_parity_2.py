from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        d = [0] * len(A)
        i, j = 0, 1
        for e in A:
            if e % 2 == 0:
                d[i], i = e, i + 2
            else:
                d[j], j = e, j + 2
        return d
