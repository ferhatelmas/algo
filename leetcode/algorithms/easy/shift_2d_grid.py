from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l = len(grid[0])
        m = [c for r in grid for c in r]
        shift = k % len(m)
        s = m[-shift:] + m[:-shift]
        return [s[i : i + l] for i in range(0, len(s), l)]
