class Solution:
    def hammingWeight(self, n):
        return bin(n)[2:].count("1")
