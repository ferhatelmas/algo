from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        ls = []
        s, e = rounds[0] - 1, rounds[-1] - 1
        while True:
            ls.append(s + 1)
            if s == e:
                break
            s = (s + 1) % n
        return sorted(ls)
