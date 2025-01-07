from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        total = 0
        for col in map(list, zip(*grid)):
            prev = -1
            for i, e in enumerate(col):
                if i == 0:
                    prev = e
                    continue
                if e > prev:
                    prev = e
                else:
                    total += prev - e + 1
                    prev += 1
        return total
