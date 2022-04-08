from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        my, mc = 0, 0
        for y in range(1950, 2051):
            c = sum(b <= y < d for b, d in logs)
            if c > mc:
                mc, my = c, y
        return my
