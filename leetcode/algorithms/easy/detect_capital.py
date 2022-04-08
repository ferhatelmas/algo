class Solution(object):
    def detectCapital(self, w):
        return len(w) < 2 or w in (w.lower(), w.upper(), w.title())
