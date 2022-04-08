class Solution:
    def makeGood(self, s: str) -> str:
        changed = True
        while changed:
            changed = False
            for i, e in enumerate(s[:-1]):
                f = s[i + 1]
                if e != f and e.lower() == f.lower():
                    changed = True
                    s = s[:i] + s[i + 2 :]
                    break
        return s
