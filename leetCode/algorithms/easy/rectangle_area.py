class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        S1 = (C-A)*(D-B)
        S2 = (G-E)*(H-F)
        if C < E or G < A or H < B or D < F:
            return S1 + S2
        x1, y1 = max(A, E), max(B, F)
        x2, y2 = min(C, G), min(D, H)

        return S1 + S2 - (x2 - x1) * (y2 - y1)
