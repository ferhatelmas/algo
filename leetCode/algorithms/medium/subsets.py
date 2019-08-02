from itertools import combinations
from typing import List


class Solution:
    def subsets(self, S: List[int]) -> List[List[int]]:
        return [list(e) for i in range(len(S) + 1) for e in combinations(sorted(S), i)]
