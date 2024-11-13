from itertools import groupby


class Solution:
    def possibleStringCount(self, word: str) -> int:
        return 1 + sum(len(list(g)) - 1 for e, g in groupby(word))
