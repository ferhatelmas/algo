from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        return [len(set(A[: i + 1]) & set(B[: i + 1])) for i in range(len(A))]
