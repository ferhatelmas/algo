class SlimeXSlimeRancher2:
    def train(self, attributes):
        m = max(attributes)
        return sum(m-e for e in attributes)
