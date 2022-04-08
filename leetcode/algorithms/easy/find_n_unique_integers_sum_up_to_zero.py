from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ls = []
        for i in range(1, n // 2 + 1):
            ls.extend([i, -i])
        if n % 2:
            ls.append(0)
        return ls
