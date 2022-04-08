from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        return [
            sum(
                abs(i - j)
                for i, a in enumerate(boxes)
                for j, b in enumerate(boxes)
                if b == "1"
            )
        ]
