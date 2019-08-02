from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res, a, b = [0], 0, 0
        for e in S:
            if e == "I":
                a += 1
                res.append(a)
            else:
                b -= 1
                res.append(b)
        return [e - b for e in res]
