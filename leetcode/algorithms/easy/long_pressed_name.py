from itertools import groupby


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_groups = [(k, len(list(g))) for k, g in groupby(name)]
        typed_groups = [(k, len(list(g))) for k, g in groupby(typed)]

        if len(name_groups) != len(typed_groups):
            return False

        for i, e in enumerate(name_groups):
            if e[0] != typed_groups[i][0]:
                return False
            if e[1] > typed_groups[i][1]:
                return False

        return True
