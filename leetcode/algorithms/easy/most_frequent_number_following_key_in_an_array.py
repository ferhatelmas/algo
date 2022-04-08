from collections import defaultdict
from operator import itemgetter
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d, l = defaultdict(int), len(nums) - 1
        for i, n in enumerate(nums):
            if n == key:
                if i < l:
                    d[nums[i + 1]] += 1
        return max(d.items(), key=itemgetter(1))[0]
