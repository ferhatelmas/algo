from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ls, m = [-1], 0
        for i, e in enumerate(reversed(arr)):
            if i:
                ls.append(m)
            m = max(m, e)
        return list(reversed(ls))
