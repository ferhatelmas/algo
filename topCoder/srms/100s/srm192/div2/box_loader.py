from itertools import permutations


class BoxLoader:
    def mostItems(self, boxX, boxY, boxZ, itemX, itemY, itemZ):
        def c(box, item):
            return reduce(lambda a, (b, i): a * (b / i), zip(box, item), 1)

        box, item = [boxX, boxY, boxZ], [itemX, itemY, itemZ]
        return max(map(lambda i: c(box, list(i)), permutations(item)))
