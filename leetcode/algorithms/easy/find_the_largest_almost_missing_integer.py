from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l, d, s = len(nums), {}, set()
        for i in range(0, l - k + 1):
            s.clear()
            for j in range(k):
                n = nums[i + j]
                if n not in s:
                    d[n] = d.get(n, 0) + 1
                s.add(n)
        return max((k for k, v in d.items() if v == 1), default=-1)
