class Solution:
    def removeElement(self, A, elem):
        i = 0
        for e in A:
            A[i] = e
            if e != elem:
                i += 1
        return i
