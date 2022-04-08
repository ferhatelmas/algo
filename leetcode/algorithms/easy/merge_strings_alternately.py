from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # cooler but slower
        # from itertools import chain
        # return "".join(chain(*zip_longest(word1, word2, fillvalue="")))
        s = ""
        for a, b in zip_longest(word1, word2, fillvalue=""):
            s = s + a + b
        return s
