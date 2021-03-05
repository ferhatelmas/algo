import re


class PunctuationCleaner:
    def clearExcess(self, document):
        return re.sub(r"!+", "!", re.sub(r"[\?!]*\?[\?!]*", "?", document))
