from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = Counter(A.split()) + Counter(B.split())
        return [k for k, v in c.items() if v == 1]
