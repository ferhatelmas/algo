from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        a, b, l, s = 1000001, 0, 0, 0
        for e in salary:
            s += e
            l += 1
            a, b = min(e, a), max(e, b)
        return (s - a - b) / (l - 2)
