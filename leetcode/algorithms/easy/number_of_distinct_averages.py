from collections import deque
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        d = deque(nums)
        while d:
            s.add((d.pop() + d.popleft()) / 2)
        return len(s)
