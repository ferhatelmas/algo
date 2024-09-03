import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ls = [[e, i] for i, e in enumerate(nums)]
        heapq.heapify(ls)
        for _ in range(k):
            it = heapq.heappop(ls)
            it[0] *= multiplier
            heapq.heappush(ls, it)
        return [e for e, _ in sorted(ls, key=lambda x: x[1])]
