from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            return sum(int(w) for w in str(n))

        return min(digit_sum(e) for e in nums)
