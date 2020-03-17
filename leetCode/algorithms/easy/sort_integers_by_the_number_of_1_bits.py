from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        count = lambda e: bin(e)[1:].count("1")
        return sorted(arr, key=lambda e: (count(e), e))
