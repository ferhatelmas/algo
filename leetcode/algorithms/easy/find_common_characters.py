from collections import Counter
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        c = Counter(A[0])
        for e in A[1:]:
            c = c & Counter(e)
        return list(c.elements())
