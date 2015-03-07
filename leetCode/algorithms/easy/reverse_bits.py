class Solution:
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1], 2)

