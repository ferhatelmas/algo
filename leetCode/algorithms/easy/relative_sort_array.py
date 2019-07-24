from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a, res = Counter(arr1), []
        for e in arr2:
            res.extend([e] * a[e])
        s = set(arr2)
        return res + sorted(chain(*([k]*v for k, v in a.items() if k not in s)))
