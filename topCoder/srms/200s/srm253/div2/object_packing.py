from operator import mul


class ObjectPacking:
    def smallBox(self, objWidth, objLength, boxWidth, boxLength):
        def p(e):
            return reduce(mul, e)

        w, l = max(objWidth, objLength), min(objWidth, objLength)
        res = sorted(
            filter(
                lambda (a, b): max(a, b) >= w and min(a, b) >= l,
                zip(boxWidth, boxLength),
            ),
            cmp=lambda x, y: cmp(p(x), p(y)),
        )
        return p(res[0]) if res else -1
