from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ls = []

        def backtrack(s, cnt):
            if cnt == n:
                ls.append(s)
                return

            for e in "01":
                if not s or e == "1" or s[-1] != "0":
                    backtrack(s + e, cnt + 1)

        backtrack("", 0)
        return ls
