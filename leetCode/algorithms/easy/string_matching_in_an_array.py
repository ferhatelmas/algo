from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ls = []
        for w in words:
            for w2 in words:
                if w != w2 and w in w2:
                    ls.append(w)
                    break
        return ls
