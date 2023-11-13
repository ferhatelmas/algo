from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i, r in enumerate(grid):
            if all(i == j or c == 1 for j, c in enumerate(r)):
                return i
        return -1
