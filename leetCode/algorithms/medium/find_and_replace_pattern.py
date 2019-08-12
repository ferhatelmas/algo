from typing import List
from string import ascii_lowercase


class Solution:
    def transform(self, s):
        d, i = {}, 0
        for e in s:
            if e not in d:
                d[e] = ascii_lowercase[i]
                i += 1
        return "".join(d[e] for e in s)

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = self.transform(pattern)
        return [w for w in words if self.transform(w) == p]
