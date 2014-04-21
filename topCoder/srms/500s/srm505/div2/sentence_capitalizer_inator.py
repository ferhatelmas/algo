class SentenceCapitalizerInator:
    def fixCaps(self, paragraph):
        return '. '.join(e.lstrip().capitalize() for e in paragraph.split('.')).rstrip()
