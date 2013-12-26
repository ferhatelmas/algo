class DietPlan:
    def chooseDinner(self, diet, breakfast, lunch):
        s, a = set(diet), set()
        for e in breakfast + lunch:
            if e not in s or e in a:
                return 'CHEATER'
            else:
                a.add(e)
        return ''.join(sorted(s-a))
