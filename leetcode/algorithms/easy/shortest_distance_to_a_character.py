from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        index = [i for i, e in enumerate(S) if e == C]
        return [min(abs(i - j) for j in index) for i, e in enumerate(S)]
