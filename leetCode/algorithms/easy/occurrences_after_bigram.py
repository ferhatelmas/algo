from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ls = text.split()
        return [c for a, b, c in zip(ls, ls[1:], ls[2:])
                if a == first and b == second]
