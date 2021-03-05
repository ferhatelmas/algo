from operator import itemgetter


class ObjectFall:
    def howLong(self, x, y, obstacles):
        o, c = map(lambda e: map(int, e.split()), obstacles), 0
        for oy, ox1, ox2 in sorted(o, key=itemgetter(0), reverse=True):
            if oy <= y:
                c += y - oy
                y = oy
                if ox1 <= x <= ox2:
                    c += 5
                    x = ox2
        return c + y if y else y
