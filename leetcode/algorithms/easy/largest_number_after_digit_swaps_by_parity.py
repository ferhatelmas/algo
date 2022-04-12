class Solution:
    def largestInteger(self, num: int) -> int:
        s = [int(e) for e in str(num)]
        odds, evens = [], []
        for e in s:
            if e % 2 == 0:
                evens.append(e)
            else:
                odds.append(e)
        evens.sort()
        odds.sort()
        n = []
        for e in s:
            if e % 2 == 0:
                n.append(evens.pop())
            else:
                n.append(odds.pop())
        return int("".join(map(str, n)))
