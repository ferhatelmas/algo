import heapq


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SummaryRanges(object):
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        heapq.heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        intervals = []
        while self.intervals:
            i = heapq.heappop(self.intervals)
            if not intervals:
                intervals.append(i)
            else:
                _, prev = intervals[-1]
                if prev.end + 1 >= i[1].start:
                    prev.end = max(prev.end, i[1].end)
                else:
                    intervals.append(i)
        self.intervals = intervals
        return [iv for v, iv in intervals]
