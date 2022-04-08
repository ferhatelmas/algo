class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([w for w in s.split("0") if w]) == 1
