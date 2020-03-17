from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = set(min(r) for r in matrix)
        cols = set(max(c) for c in zip(*matrix))
        return list(rows & cols)
