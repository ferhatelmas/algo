from itertools import groupby


class Solution:
    def countKeyChanges(self, s: str) -> int:
        return len(list(groupby(s, key=lambda x: x.lower()))) - 1
