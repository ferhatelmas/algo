from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s = {b for _, b in edges}
        return [i for i in range(n) if i not in s]
