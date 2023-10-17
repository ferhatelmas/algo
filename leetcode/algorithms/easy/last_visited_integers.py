from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ls, res, last, n = [], [], -1, -1
        for w in words:
            if w != "prev":
                ls.append(int(w))
                n += 1
                last = n
            else:
                if last >= 0:
                    res.append(ls[last])
                    last -= 1
                else:
                    res.append(-1)
        return res
