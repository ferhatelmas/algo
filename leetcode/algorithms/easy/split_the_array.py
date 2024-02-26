from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all(v <= 2 for v in Counter(nums).values())
