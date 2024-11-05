class Solution:
    def isBalanced(self, num: str) -> bool:
        c = 0
        for i, e in enumerate(num):
            if i % 2:
                c += int(e)
            else:
                c -= int(e)
        return c == 0
