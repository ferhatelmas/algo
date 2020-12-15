from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        container = set(allowed)
        return sum(not (set(w) - container) for w in words)
