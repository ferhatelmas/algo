from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        r = [0, 0]
        for i, v in enumerate(bin(n)[:1:-1]):
            if v == "1":
                j = i % 2
                r[j] += 1
        return r
