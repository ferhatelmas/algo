from itertools import chain
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(c)) for c in col) for col in chain(zip(*grid))]
