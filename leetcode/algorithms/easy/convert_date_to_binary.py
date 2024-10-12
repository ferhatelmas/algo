class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(bin(int(e))[2:] for e in date.split("-"))
