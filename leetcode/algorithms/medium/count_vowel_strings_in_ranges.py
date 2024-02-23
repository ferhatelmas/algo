from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ws = [w[0] in "aeiou" and w[-1] in "aeiou" for w in words]
        ls, c = [], 0
        for w in ws:
            if w:
                c += 1
            ls.append(c)
        return [ls[j] - (ls[i - 1] if i > 0 else 0) for i, j in queries]
