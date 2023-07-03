class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ls = len(s)
        if ls != len(goal):
            return False
        d1, d2, c = [], [], 0
        for a, b in zip(s, goal):
            if a != b:
                d1.append(a)
                d2.append(b)
                c += 1
            if c > 2:
                return False
        return (d1 and sorted(d1) == sorted(d2)) or (not d1 and len(set(s)) < ls)
