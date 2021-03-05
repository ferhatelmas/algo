class TwoWaysSorting:
    def sortingMethod(self, stringList):
        s1, s2 = tuple(sorted(stringList)), tuple(sorted(stringList, key=len))
        if stringList == s1 == s2:
            return "both"
        elif stringList == s1:
            return "lexicographically"
        elif stringList == s2:
            return "lengths"
        return "none"
