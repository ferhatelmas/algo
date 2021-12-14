class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        for i in range(0, len(rings) - 1, 2):
            r = rings[i]
            rod = rings[i + 1]
            if rod not in rods:
                rods[rod] = set()
            rods[rod].add(r)

        return sum(len(r) == 3 for r in rods.values())
