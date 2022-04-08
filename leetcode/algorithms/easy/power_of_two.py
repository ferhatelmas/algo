class Solution:
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        return list(bin(n)[2:]).count("1") == 1
