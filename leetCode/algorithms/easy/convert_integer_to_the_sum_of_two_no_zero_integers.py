from typing import List


class Solution:
    def no_zero(self, n):
        return "0" not in str(n)

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.no_zero(i):
                j = n - i
                if self.no_zero(j):
                    return [i, n - i]
