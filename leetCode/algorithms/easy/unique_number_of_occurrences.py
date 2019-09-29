from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ls = list(Counter(arr).values())
        return len(ls) == len(set(ls))
