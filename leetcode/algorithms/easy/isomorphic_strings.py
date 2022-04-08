class Solution:
    def isIsomorphic(self, s, t):
        m, n = {}, set()
        for a, b in zip(s, t):
            if a in m:
                if m[a] != b:
                    return False
            elif b in n:
                return False
            else:
                m[a] = b
                n.add(b)
        return True
