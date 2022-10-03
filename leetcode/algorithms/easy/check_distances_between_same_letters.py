from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}
        a = ord("a")
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                if distance[ord(c) - a] != i - d[c] - 1:
                    return False
        return True
