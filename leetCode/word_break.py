class Solution:
    def wordBreak(self, s, dict):
        full_dict = set(''.join(dict))
        if not all(e in full_dict for e in set(s)):
            return False
        return self.solve(s, dict, len(s))

    def solve(self, s, dict, l):
        return True if not s else any(s[:i] in dict and self.solve(s[i:], dict, l-i)
                                      for i in xrange(l, 0, -1))