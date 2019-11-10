from collections import defaultdict
from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols = defaultdict(int), defaultdict(int)
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        return sum((rows[i] + cols[j]) % 2 for i in range(n) for j in range(m))
