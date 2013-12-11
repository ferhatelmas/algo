import re

class Pronunciation:
    def canPronounce(self, words):
        def is_problem(w):
            return re.search(r'[^aeiou]{3,}', w) or \
                   any(map(lambda e: len(set(e)) != 1, re.findall(r'[aeiou]{2,}', w)))

        for word in words:
            if is_problem(word.lower()):
                return word
        return ''
