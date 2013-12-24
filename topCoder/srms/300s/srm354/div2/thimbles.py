class Thimbles:
    def thimbleWithBall(self, swaps):
        i = 1
        for s in swaps:
            a, b = map(int, s.split('-'))
            if a == i:
                i = b
            elif b == i:
                i = a
        return i
