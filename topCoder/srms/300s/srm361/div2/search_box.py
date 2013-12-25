import re

class SearchBox:
    def find(self, text, search, wholeWord, start):
        if wholeWord == 'Y':
            search = r'\b%s\b' % search
        m = re.compile(search).search(text, start)
        return m.start() if m else -1
