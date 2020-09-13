from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        s = sum(mat[i][i] + mat[i][l - 1 - i] for i in range(l))
        if l % 2 == 1:
            s -= mat[l // 2][l // 2]
        return s
