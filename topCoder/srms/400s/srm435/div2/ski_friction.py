class SkiFriction:
    def bestPosition(self, skiFriction, pathFriction):
        s = 0
        for i in xrange(len(pathFriction) - len(skiFriction)):
            s += max(int(a) + int(b) for a, b in zip(skiFriction, pathFriction[i:]))
        return s
