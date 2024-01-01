from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        has = False
        for i in nums:
            if i % 2 == 0:
                if has:
                    return True
                has = True
        return False
