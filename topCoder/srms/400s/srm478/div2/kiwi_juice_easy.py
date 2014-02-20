class KiwiJuiceEasy:
    def thePouring(self, capacities, bottles, fromId, toId):
        bottles = list(bottles)
        for f, t in zip(fromId, toId):
            m = min(capacities[t] - bottles[t], bottles[f])
            bottles[t] += m
            bottles[f] -= m
        return bottles
