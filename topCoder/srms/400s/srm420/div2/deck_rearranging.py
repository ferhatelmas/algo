class DeckRearranging:
    def rearrange(self, deck, above):
        ls = []
        for e, a in zip(deck, above):
            ls.insert(a, e)
        return ''.join(ls)
