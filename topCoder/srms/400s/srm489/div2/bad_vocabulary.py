import re

class BadVocabulary:
    def count(self, badPrefix, badSuffix, badSubstring, vocabulary):
        r = re.compile(r'.+{}.+'.format(badSubstring))
        def is_bad(s):
            return s.startswith(badPrefix) or s.endswith(badSuffix) or bool(re.match(r, s)  )
        return sum(map(is_bad, vocabulary))
