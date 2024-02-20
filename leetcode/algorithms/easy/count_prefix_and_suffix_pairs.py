from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i, s1 in enumerate(words):
            for j, s2 in enumerate(words):
                if j <= i:
                    continue
                cnt += s2.startswith(s1) and s2.endswith(s1)
        return cnt
