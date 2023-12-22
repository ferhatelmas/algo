from itertools import chain
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = [], []
        for e in nums:
            if e > 0:
                p.append(e)
            else:
                n.append(e)
        return chain(*zip(p, n))
