class Solution(object):
    def findComplement(self, num):
        return int("".join("01" [e == "0"] for e in bin(num)[2:]), 2)
