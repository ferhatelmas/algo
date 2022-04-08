class Solution:
    def largestRectangleArea(self, height):
        s, m, l, i = [], 0, len(height), 0
        while i < l:
            if not s or height[i] >= height[s[-1]]:
                s.append(i)
                i += 1
            else:
                m = max(m, self.area(height, i, s))
        while s:
            m = max(m, self.area(height, i, s))
        return m

    def area(self, height, i, s):
        return height[s.pop()] * (i if not s else i - s[-1] - 1)
