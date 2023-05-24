from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.h.append(val)
        self.h.sort()
        return self.h[-self.k]
