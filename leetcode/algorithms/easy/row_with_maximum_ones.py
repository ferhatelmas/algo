from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, j = -1, -1
        for i, row in enumerate(mat):
            n = sum(row)
            if n > m:
                m, j = n, i
        return [j, m]
