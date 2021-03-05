class SimpleWordGame:
    def points(self, player, dictionary):
        return sum(len(e) ** 2 for e in set(player) if e in dictionary)
