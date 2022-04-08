from typing import List


class Solution:
    def canBeEqual(self, t: List[int], s: List[int]) -> bool:
        return len(t) != len(s) and all(a == b for a, b in zip(sorted(t), sorted(s)))
