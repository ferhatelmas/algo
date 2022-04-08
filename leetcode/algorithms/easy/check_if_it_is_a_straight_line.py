from typing import List


class Solution:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        if len(coords) == 2:
            return True
        x1, y1 = coords[0]
        x2, y2 = coords[1]
        return all(
            (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1) for (x3, y3) in coords[2:]
        )
