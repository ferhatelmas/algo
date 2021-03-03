from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = 0
        if ruleKey == 'color':
            i = 1
        elif ruleKey == 'name':
            i = 2
        return sum(j[i] == ruleValue for j in items)
