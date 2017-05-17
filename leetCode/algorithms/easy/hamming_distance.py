import operator


class Solution(object):
    def hammingDistance(self, x, y):
        return bin(operator.xor(x, y)).count('1')
