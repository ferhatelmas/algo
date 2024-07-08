class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        l = len(s)
        return "".join(s[(i + k) % l] for i in range(0, l))
