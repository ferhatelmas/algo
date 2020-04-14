from collections import deque
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ls, res = deque(list(range(1, m + 1))), []
        for q in queries:
            res.append(ls.index(q))
            ls.remove(q)
            ls.appendleft(q)
        return res
