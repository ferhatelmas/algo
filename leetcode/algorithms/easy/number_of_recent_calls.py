from collections import deque


class RecentCounter:
    def __init__(self):
        self.t = deque([])

    def ping(self, t: int) -> int:
        self.t.append(t)
        a = self.t.popleft()
        while a < t - 3000:
            a = self.t.popleft()
        if a >= t - 3000:
            self.t.appendleft(a)
        return len(self.t)
