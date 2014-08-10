class RectangularGrid:
    def countRectangles(self, width, height):
        return sum(
            (width - i + 1) * (height - j + 1)
            for i in xrange(1, width+1)
            for j in xrange(1, height+1)
            if i != j
        )
