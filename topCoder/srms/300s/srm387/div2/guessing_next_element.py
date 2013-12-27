class GuessingNextElement:
    def guess(self, A):
        if A[2] - A[1] == A[1] - A[0]:
            return A[1] - A[0] + A[-1]
        return A[-1] * (A[1] / A[0])
