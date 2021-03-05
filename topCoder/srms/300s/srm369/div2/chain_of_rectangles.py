class ChainOfRectangles:
    def getMaximalArea(self, width, height, color):
        r, g, b = 0, 0, 0
        ls = [w * h for h, w in zip(height, width)]
        for i, (l, c) in enumerate(zip(ls, color)):
            area = l - max([0] + ls[i + 1 : i + 2])
            if c == "R":
                r += area
            elif c == "G":
                g += area
            else:
                b += area
        return max(r, g, b)
