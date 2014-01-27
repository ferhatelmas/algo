class ReverseMagicalSource:
    def find(self, source, A):
        s = 0
        while s <= A:
            s += source
            source *= 10
        return s
