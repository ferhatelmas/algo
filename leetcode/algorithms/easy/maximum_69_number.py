class Solution:
    def maximum69Number(self, num: int) -> int:
        ls, changed = [], False
        for e in str(num):
            if not changed and e == "6":
                ls.append("9")
                changed = True
            else:
                ls.append(e)
        return int("".join(ls))
