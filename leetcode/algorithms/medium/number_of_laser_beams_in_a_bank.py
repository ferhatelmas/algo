from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        s, prev = 0, None
        for i, r in enumerate(bank):
            c = r.count("1")
            if c == 0:
                continue
            if prev is None:
                prev = c
            else:
                s += c * prev
                prev = c
        return s
