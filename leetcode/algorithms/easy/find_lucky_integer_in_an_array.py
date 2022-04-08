from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max(chain((k for k, v in Counter(arr).items() if k == v), [-1]))
