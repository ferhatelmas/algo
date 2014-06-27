class ColorfulBricks:
    def countLayouts(self, bricks):
        c = len(set(bricks))
        return 0 if c > 2 else c
