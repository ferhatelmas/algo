class Solution:
    def removeDuplicates(self, A):
        if A:
            i = 0
            for j, e in enumerate(A):
                if e != A[i]:
                    i += 1
                    A[i] = e
            return i + 1
        return 0
