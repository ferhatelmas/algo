from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        g, e, l = [], [], []
        for n in nums:
            if n == pivot:
                e.append(n)
            elif n > pivot:
                g.append(n)
            else:
                l.append(n)
        return l + e + g
