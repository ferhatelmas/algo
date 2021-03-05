class DocumentSearch:
    def nonIntersecting(self, doc, search):
        doc = "".join(doc)
        i, l, c = doc.find(search), len(search), 0
        while i > -1:
            c += 1
            doc = doc[i + l :]
            i = doc.find(search)
        return c
