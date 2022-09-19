from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)

        for path in paths:
            parts = path.split(" ")
            for p in parts[1:]:
                name, content = p.split("(")
                content = content.rstrip(")")
                contents[content].append(parts[0] + "/" + name)
        return [ls for ls in contents.values() if len(ls) > 1]
