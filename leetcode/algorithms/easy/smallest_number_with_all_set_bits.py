class Solution:
    def smallestNumber(self, n: int) -> int:
        changed, s = False, []
        for e in bin(n)[2:]:
            if e == "0":
                changed = True
            s.append("1")
        if not changed:
            return n
        return int("".join(s), 2)
