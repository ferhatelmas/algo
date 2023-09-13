class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        for w in s.split(" "):
            try:
                d = int(w)
                if prev and d <= prev:
                    return False
                prev = d
            except:  # noqa: E722
                pass
        return True
