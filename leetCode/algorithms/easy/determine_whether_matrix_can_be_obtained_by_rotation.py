from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if all(a == b for a, b in zip(mat, target)):
                return True
            mat = [list(ls)[::-1] for ls in zip(*mat)]
        return False
