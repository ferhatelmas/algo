class TrainingCamp:
    def determineSolvers(self, attendance, problemTopics):
        return [
            ''.join(('X', '-')[any(j == 'X' and i != 'X' for i, j in zip(s, t))]
                    for t in problemTopics) for s in attendance
        ]
