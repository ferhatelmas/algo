from operator import itemgetter
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tops = sorted((n, i) for i, n in enumerate(nums))[-k:]
        return [n for n, i in sorted(tops, key=itemgetter(1))]
