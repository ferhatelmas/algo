from typing import List


class Solution:
    def isWinner(self, p1: List[int], p2: List[int]) -> int:
        def score(p: List[int]) -> int:
            s = 0
            for i, n in enumerate(p):
                if (i > 0 and p[i - 1] == 10) or (i > 1 and p[i - 2] == 10):
                    s += n
                s += n
            return s

        s1 = score(p1)
        s2 = score(p2)
        return 0 if s1 == s2 else [1, 2][s1 < s2]
