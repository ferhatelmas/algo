from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for r in matrix:
            if len(set(r)) != n:
                return False
        for r in zip(*matrix):
            if len(set(r)) != n:
                return False
        return True
