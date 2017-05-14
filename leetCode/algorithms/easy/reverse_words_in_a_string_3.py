class Solution(object):
    def reverseWords(self, s):
        return ' '.join(w[::-1] for w in s.split())
