from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = c.most_common(1)[0][1]
        return sum(n for a, b in c.items() if b == n)
