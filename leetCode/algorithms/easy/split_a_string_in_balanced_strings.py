class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt, c = 0, 0
        for e in s:
            if e == 'L':
                c += 1
            else:
                c -= 1
            if c == 0:
                cnt += 1
        return cnt
