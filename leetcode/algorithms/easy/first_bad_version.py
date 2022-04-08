def isBadVersion(n):
    """Provided API call"""
    pass


class Solution:
    def firstBadVersion(self, n):
        l = 1
        m = (n + l) // 2
        while l < n:
            if isBadVersion(m):
                n = m
            else:
                l = m + 1
            m = (n + l) // 2
        return m
