from typing import List
from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        d = deque(arr)
        prev, c = -1, 0
        while c < k:
            a, b = d[0], d[1]
            if a > b:
                d.popleft()
                d.append(d.popleft())
                d.appendleft(a)
            else:
                d.append(d.popleft())

            m = max(a, b)
            if m == prev:
                c += 1
            else:
                prev, c = m, 1
        return prev
