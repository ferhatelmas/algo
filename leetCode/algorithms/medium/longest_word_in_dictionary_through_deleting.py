class Solution(object):
    def contains(self, s, ls, w, lw):
        if lw > ls:
            return False
        elif lw == ls and w == s:
            return True
        start = -1
        for i in range(lw):
            start = s.find(w[i], start + 1)
            if start == -1:
                return False
        return True

    def findLongestWord(self, s, d):
        ls = len(s)
        for w in sorted(d, key=lambda x: (-len(x), x)):
            if self.contains(s, ls, w, len(w)):
                return w
        return ""
