import bisect


class MedianFinder:
    def __init__(self):
        self.n = 0
        self.ls = []

    def addNum(self, num):
        self.ls.insert(bisect.bisect(self.ls, num), num)
        self.n += 1

    def findMedian(self):
        i = self.n // 2
        if self.n % 2:
            return self.ls[i]
        return sum(self.ls[i-1:i+1]) / 2.0
