from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ls = [first]
        for e in encoded:
            ls.append(e ^ ls[-1])
        return ls
