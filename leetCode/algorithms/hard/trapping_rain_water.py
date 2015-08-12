class Solution:
    def trap(self, height):
        l, r, h, w = 0, len(height) - 1, 0, 0
        while l < r:
            if height[l] < height[r]:
                low = height[l]
                l += 1
            else:
                low = height[r]
                r -= 1
            h = max(h, low)
            w += h - low
        return w
