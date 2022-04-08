from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a, b = set(), set()
        for i, j in paths:
            a.add(i)
            b.add(j)
        return (b - a).pop()
