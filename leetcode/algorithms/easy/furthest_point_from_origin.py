class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, n = 0, 0, 0
        for e in moves:
            l += e == "L"
            r += e == "R"
            n += e == "_"
        return abs(l - r) + n
