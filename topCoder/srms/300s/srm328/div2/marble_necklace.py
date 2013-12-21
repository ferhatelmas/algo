class MarbleNecklace:
    def normalize(self, necklace):
        a = []
        for i in xrange(len(necklace)):
            a.append(necklace[i:] + necklace[:i])
            a.append(necklace[:i][::-1] + necklace[i:][::-1])
        return sorted(a)[0]
