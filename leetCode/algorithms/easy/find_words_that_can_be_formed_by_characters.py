from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c, s = Counter(chars), 0
        for w in words:
            if all(k in c and c[k] >= v for k, v in Counter(w).items()):
                s += len(w)
        return s
