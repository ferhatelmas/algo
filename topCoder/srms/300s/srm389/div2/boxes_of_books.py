class BoxesOfBooks:
    def boxes(self, weights, maxWeight):
        c, p = 0, 0
        for w in weights:
            if w > p:
                c += 1
                p = maxWeight
            p -= w
        return c
