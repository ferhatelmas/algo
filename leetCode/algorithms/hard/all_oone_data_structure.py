from operator import itemgetter


class AllOne:
    def __init__(self):
        self.d = {}

    def inc(self, key: str) -> None:
        self.d[key] = self.d.get(key, 0) + 1

    def dec(self, key: str) -> None:
        n = self.d.get(key, 1)
        if n == 1:
            self.d.pop(key, None)
        else:
            self.d[key] = n - 1

    def getMaxKey(self) -> str:
        if not self.d:
            return ""
        return sorted(self.d.items(), key=itemgetter(1))[-1][0]

    def getMinKey(self) -> str:
        if not self.d:
            return ""
        return sorted(self.d.items(), key=itemgetter(1))[0][0]
