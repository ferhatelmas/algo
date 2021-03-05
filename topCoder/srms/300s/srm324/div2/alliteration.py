from itertools import groupby


class Alliteration:
    def count(self, words):
        return sum(
            map(
                lambda (k, g): len(list(g)) > 1,
                groupby(map(lambda w: w[:1].lower(), words)),
            )
        )
