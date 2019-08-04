from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines, line = 1, 0
        for e in S:
            i = widths[ord(e) - ord("a")]
            if line + i > 100:
                lines, line = lines + 1, i
            else:
                line += i
        return [lines, line]
