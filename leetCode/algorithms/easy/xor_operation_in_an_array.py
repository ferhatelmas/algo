class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        v = start
        for i in range(1, n):
            v ^= start + 2 * i
        return v
