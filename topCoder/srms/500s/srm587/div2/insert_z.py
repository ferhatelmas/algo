class InsertZ:
    def canTransform(self, init, goal):
        return 'Yes' if goal.replace('z', '') == init else 'No'
