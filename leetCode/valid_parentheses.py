class Solution:
    def isValid(self, s):
        p, ss = [], '[{('
        for e in s:
            if e in ']})':
                if not p or ss.index(p[-1]) != ']})'.index(e):
                    return False
                else:
                    p.pop()
            else:
                p.append(e)
        return not bool(p)
