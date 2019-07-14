class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return A == B == "" or any(A[i:] + A[:i] == B for i in range(len(A)))
