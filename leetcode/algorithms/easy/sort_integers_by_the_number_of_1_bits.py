from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count(e):
            return bin(e)[1:].count("1")

        return sorted(arr, key=lambda e: (count(e), e))
