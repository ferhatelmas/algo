from operator import itemgetter
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        powers = sorted(((i, sum(ls)) for i, ls in enumerate(mat)), key=itemgetter(1))
        return [p[0] for p in powers[:k]]
