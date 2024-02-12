from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        l = len(matrix)
        for i, r in enumerate(matrix):
            for j, e in enumerate(r):
                if e == -1:
                    matrix[i][j] = max(matrix[k][j] for k in range(0, l))
        return matrix
