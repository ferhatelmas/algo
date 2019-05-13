class Solution:
    def findPeakElement(self, num):
        l = len(num) - 1
        for i, e in enumerate(num):
            if ((i == 0 or e > num[i - 1]) and (i == l or e > num[i + 1])):
                return i
        return 0
