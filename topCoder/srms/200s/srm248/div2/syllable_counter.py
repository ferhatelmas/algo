import re

class SyllableCounter:
    def countSyllables(self, word):
        return len(re.findall(r'[aeiou]+', word.lower()))
