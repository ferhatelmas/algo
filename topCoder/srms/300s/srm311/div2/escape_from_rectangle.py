class EscapeFromRectangle:
    def shortest(self, x, y, w, h):
        return min(x, y, w-x, h-y)
