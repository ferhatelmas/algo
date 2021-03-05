class FuelConsumption:
    def maximalDistance(self, velocities, consumptions, fuel):
        return max(
            map(lambda (v, c): v * float(fuel) / c, zip(velocities, consumptions))
        )
