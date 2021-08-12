from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        w = ""
        for e in words:
            w += e
            if w == s:
                return True
        return False
