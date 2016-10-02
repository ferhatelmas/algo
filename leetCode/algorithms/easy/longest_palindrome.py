import collections


class Solution(object):
    def longestPalindrome(self, s):
        c = odd = 0
        for _, n in collections.Counter(s).items():
            if n % 2:
                odd, n = True, n - 1
            c += n
        return c + odd
