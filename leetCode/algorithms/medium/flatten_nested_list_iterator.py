from collections import deque


class NestedIterator(object):
    def __init__(self, nestedList):
        self.q = deque([])
        self.processList(nestedList)

    def processList(self, ls):
        for e in ls:
            if e.isInteger():
                self.q.append(e.getInteger())
            else:
                self.processList(e.getList())

    def next(self):
        return self.q.popleft()

    def hasNext(self):
        return bool(self.q)
