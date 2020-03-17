from collections import Counter
from string import ascii_lowercase
from typing import Counter as CounterType, List


class Solution:
    def loop(self, c: CounterType, ls: List[str], looper: str) -> List[str]:
        for e in looper:
            n = c[e]
            if n > 0:
                ls.append(e)
                n -= 1
                if n > 0:
                    c[e] = n
                else:
                    del c[e]
        return ls

    def sortString(self, s: str) -> str:
        c = Counter(s)
        res = []
        reversed = ascii_lowercase[::-1]
        while c:
            res = self.loop(c, res, ascii_lowercase)
            res = self.loop(c, res, reversed)
        return "".join(res)

