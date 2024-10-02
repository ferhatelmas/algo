from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ls = []
        for i, _ in enumerate(height):
            if i and height[i - 1] > threshold:
                ls.append(i)
        return ls
