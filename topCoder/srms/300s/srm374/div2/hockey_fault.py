class HockeyFault:
    def numPlayers(self, width, height, x, y, px, py):
        def in_rec(i, j):
            return x <= i <= x+width and y <= j <= y+height
        def in_circles(i, j):
            return (((i-x)**2 + (j-y-height/2.0)**2)**.5 <= height/2.0 or
                    ((i-x-width)**2 + (j-y-height/2.0)**2)**.5 <= height/2.0)
        return sum(1 for i, j in zip(px, py) if in_rec(i, j) or in_circles(i, j))
