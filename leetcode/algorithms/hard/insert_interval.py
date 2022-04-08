import bisect
import operator


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        i = bisect.bisect([e.start for e in intervals], newInterval.start)
        intervals.insert(i, newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=operator.attrgetter("start"))
        res = []
        s, e = intervals[0].start, intervals[0].end
        for interval in intervals:
            if interval.start <= e:
                e = max(e, interval.end)
            else:
                res.append(Interval(s, e))
                s, e = interval.start, interval.end
        res.append(Interval(s, e))
        return res
