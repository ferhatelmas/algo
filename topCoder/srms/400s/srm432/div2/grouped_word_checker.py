from itertools import groupby

class GroupedWordChecker:
    def howMany(self, words):
        def is_grouped(w):
            s = set()
            for k, _ in groupby(w):
                if k in s:
                    return False
                s.add(k)
            return True
        return sum(map(is_grouped, words))
