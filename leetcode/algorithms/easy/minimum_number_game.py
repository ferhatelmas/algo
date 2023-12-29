from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr, p = [], -1
        for n in nums:
            if p == -1:
                p = n
                continue
            arr.append(n)
            arr.append(p)
            p = -1
        return arr
