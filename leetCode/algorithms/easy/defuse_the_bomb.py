from typing import List


class Solution:
    def my_sum(self, code, l, s, e):
        return sum(code[(i + l) % l] for i in range(s + l, e + l))

    def decrypt(self, code: List[int], k: int) -> List[int]:
        ls, l = [], len(code)
        for i, e in enumerate(code):
            if k > 0:
                n = self.my_sum(code, l, i + 1, i + k + 1)
            elif k < 0:
                n = self.my_sum(code, l, i + k, i)
            else:
                n = 0
            ls.append(n)
        return ls
