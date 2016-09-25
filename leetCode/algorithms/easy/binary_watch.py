class Solution(object):
    def readBinaryWatch(self, num):
        res = []
        for i in range(12):
            a = bin(i)[2:].count("1")
            for j in range(60):
                b = bin(j)[2:].count("1")
                if a + b == num:
                    res.append("{:d}:{:02d}".format(i, j))
        return res
