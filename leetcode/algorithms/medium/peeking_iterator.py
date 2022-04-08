class PeekingIterator:
    def __init__(self, iterator):
        self.i = iterator
        self.v = None

    def peek(self):
        if self.v:
            return self.v
        self.v = self.i.next()
        return self.v

    def next(self):
        if self.v is None:
            return self.i.next()
        v = self.v
        self.v = None
        return v

    def hasNext(self):
        if self.v is None:
            return self.i.hasNext()
        return True
