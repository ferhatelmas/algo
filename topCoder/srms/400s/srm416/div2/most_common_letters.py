from itertools import groupby
from operator import itemgetter


class MostCommonLetters:
    def listMostCommon(self, text):
        ls = [
            (k, len(list(g)))
            for k, g in groupby(sorted("".join(text).replace(" ", "")))
        ]
        m = max(ls, key=itemgetter(1, 0))[1]
        return "".join([k for k, l in ls if l == m])
