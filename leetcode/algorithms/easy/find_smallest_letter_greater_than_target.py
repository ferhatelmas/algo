from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = ""
        for i, e in enumerate(letters):
            if e > target and (s == "" or e < s):
                s = e
        return s if s else letters[0]
