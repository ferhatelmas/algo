class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(1 for e in S if e in J)
