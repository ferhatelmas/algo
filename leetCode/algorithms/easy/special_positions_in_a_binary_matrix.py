from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [sum(col) for col in zip(*mat)]

        count = 0
        for i, row in enumerate(mat):
            if rows[i] != 1:
                continue
            for j, col in enumerate(row):
                if col == 1 and cols[j] == 1:
                    count += 1
                    continue
        return count
