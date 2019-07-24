class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        c, res, inc = 0, [], {'(': 1, ')': -1}
        for e in S:
            v = inc[e]
            if v == 1 and c > 0 or v == -1 and c > 1:
                res.append(e)
            c += v
        return ''.join(res)
