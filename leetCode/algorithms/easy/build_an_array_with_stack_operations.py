from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ls, j, l = [], 0, len(target)
        for i in range(1, n + 1):
            ls.append("Push")
            if target[j] == i:
                j += 1
                if j == l:
                    return ls
            else:
                ls.append("Pop")
        return ls
