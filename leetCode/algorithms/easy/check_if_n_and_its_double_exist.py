from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for e in arr:
            if e * 2 in d or (e % 2 == 0 and e / 2 in d):
                return True
            d.add(e)
        return False
