from typing import List
from itertools import zip_longest


class Solution:
    def printVertically(self, s: str) -> List[str]:
        return ["".join(w).rstrip() for w in zip_longest(*s.split(), fillvalue=" ")]
