class Solution:
    def reverseParentheses(self, s: str) -> str:
        ls = [[]]
        for e in s:
            if e == "(":
                ls.append([])
            elif e == ")":
                w = reversed(ls.pop())
                ls[-1] += w
            else:
                ls[-1].append(e)
        return "".join(ls.pop())
