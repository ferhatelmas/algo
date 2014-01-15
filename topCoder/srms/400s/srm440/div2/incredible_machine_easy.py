class IncredibleMachineEasy:
    def gravitationalAcceleration(self, height, T):
        return (sum((2*h)**0.5 for h in height) / T)**2
