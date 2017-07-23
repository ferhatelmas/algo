class Solution(object):
    def countSegments(self, s):
        return len([w for w in s.split(" ") if w])
