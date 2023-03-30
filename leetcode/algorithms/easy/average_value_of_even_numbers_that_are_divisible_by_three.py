from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s, c = 0, 0
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                s += n
                c += 1
        return 0 if c == 0 else s // c
