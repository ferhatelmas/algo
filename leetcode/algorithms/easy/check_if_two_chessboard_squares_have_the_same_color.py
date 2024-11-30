class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return (
            (coordinate1[0] in "aceg" and coordinate1[1] in "1357")
            or (coordinate1[0] in "bdfh" and coordinate1[1] in "2468")
        ) == (
            (coordinate2[0] in "aceg" and coordinate2[1] in "1357")
            or (coordinate2[0] in "bdfh" and coordinate2[1] in "2468")
        )
