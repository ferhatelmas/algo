class Solution:
    def maxArea(self, height):
        i, j, w = 0, len(height) - 1, 0
        while i < j:
            h = min(height[i], height[j])
            w = max(w, (j - i) * h)
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return w
