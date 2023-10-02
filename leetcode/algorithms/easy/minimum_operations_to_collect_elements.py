from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set(i for i in range(1, k + 1))
        d = set()
        c = 0
        while True:
            c += 1
            d.add(nums.pop())
            if s.issubset(d):
                return c
        return len(nums)
