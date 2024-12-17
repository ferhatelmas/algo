from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        for e in sorted(set(nums)):
            if e < k:
                return -1
            if e > k:
                cnt += 1
        return cnt
