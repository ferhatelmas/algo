class BishopMove:
    def howManyMoves(self, r1, c1, r2, c2):
        def is_in_range(r, c):
            for i in xrange(8):
                if (
                    (r2 == r + i and c2 == c + i)
                    or (r2 == r + i and c2 == c - i)
                    or (r2 == r - i and c2 == c + i)
                    or (r2 == r - i and c2 == c - i)
                ):
                    return True
            return False

        if r1 == r2 and c1 == c2:
            return 0
        if is_in_range(r1, c1):
            return 1
        for i in xrange(8):
            if (
                is_in_range(r1 + i, c1 + i)
                or is_in_range(r1 + i, c1 - i)
                or is_in_range(r1 - i, c1 + i)
                or is_in_range(r1 - i, c1 - i)
            ):
                return 2
        return -1
