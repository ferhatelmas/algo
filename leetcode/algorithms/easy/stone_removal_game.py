class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice, c = False, 10
        while n >= c and c > 0:
            n -= c
            alice = not alice
            c -= 1
        return alice
