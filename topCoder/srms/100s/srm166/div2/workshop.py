import itertools


class Workshop:
    def pictureFrames(self, pieces):
        def is_valid(t):
            t = sorted(t)
            return (t[0] > t[2] - t[1]) and (t[2] < t[0] + t[1])

        return len(filter(is_valid, itertools.combinations(pieces, 3)))
