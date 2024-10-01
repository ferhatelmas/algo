from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ls, s = [], set()
        for e in nums:
            if e in s:
                ls.append(e)
                continue
            s.add(e)
        return ls
