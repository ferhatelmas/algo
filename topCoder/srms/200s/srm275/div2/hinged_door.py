class HingedDoor:
    def numSwings(self, initialAngle, reduction):
        c, r = 0, 1/float(reduction)
        while initialAngle > 5:
            print initialAngle
            initialAngle *= r
            c += 1
        return c
