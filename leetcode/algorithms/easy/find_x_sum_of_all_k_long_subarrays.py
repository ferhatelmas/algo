from typing import List
from collections import Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xsum(ls: List[int]) -> int:
            return sum(
                e * c for e, c in Counter(sorted(ls, reverse=True)).most_common(x)
            )

        return [xsum(nums[i : i + k]) for i in range(0, len(nums) - k + 1)]
