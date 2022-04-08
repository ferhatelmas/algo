from itertools import groupby


class Solution(object):
    def checkRecord(self, s):
        absent = s.count("A") > 1
        late = any(len(list(g)) > 2 for k, g in groupby(s) if k == "L")
        return not absent and not late
