class TopFox:
    def possibleHandles(self, familyName, givenName):
        s = set()
        for i in xrange(1, len(familyName)+1):
            for j in xrange(1, len(givenName)+1):
                s.add(familyName[:i] + givenName[:j])
        return len(s)
