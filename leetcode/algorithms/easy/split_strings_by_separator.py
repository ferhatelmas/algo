from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for w in words:
            for e in w.split(separator):
                if e:
                    res.append(e)
        return res
