class Solution:
    def partitionString(self, s: str) -> int:
        cnt, w = 0, set()
        for e in s:
            if e in w:
                cnt += 1
                w.clear()
            w.add(e)
        return cnt + 1 if w else cnt
