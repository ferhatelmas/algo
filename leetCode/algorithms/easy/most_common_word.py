import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c = Counter(e for e in re.split(r'[ \'!?,;.]+', paragraph.lower())
                    if e and e not in banned)
        return c.most_common(1)[0][0]
