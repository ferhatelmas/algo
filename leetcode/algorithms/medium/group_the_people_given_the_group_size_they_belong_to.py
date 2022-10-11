from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i, e in enumerate(groupSizes):
            if e in d:
                ls = d[e][-1]
                if len(ls) < e:
                    ls.append(i)
                else:
                    d[e].append([i])
            else:
                d[e] = [[i]]

        return [ls for lss in d.values() for ls in lss]
