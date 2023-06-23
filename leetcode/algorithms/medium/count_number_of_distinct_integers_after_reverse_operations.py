from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()
        for e in nums:
            s.add(e)
            s.add(int(str(e)[::-1]))
        return len(s)
