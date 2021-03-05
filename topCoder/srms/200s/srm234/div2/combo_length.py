from itertools import groupby


class ComboLength:
    def howLong(self, moves):
        return max(map(lambda (k, g): len(list(g)), groupby(moves)))
