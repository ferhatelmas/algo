from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = sum(apple)
        capacity.sort(reverse=True)
        for i, e in enumerate(capacity):
            if e >= n:
                return i + 1
            n -= e
        return 0
