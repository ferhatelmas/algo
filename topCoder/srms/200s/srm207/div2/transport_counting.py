class TransportCounting:
    def countBuses(self, speed, positions, velocities, time):
        me = time * speed
        return len(
            filter(
                lambda (p, v): p + time * v <= me or p == 0, zip(positions, velocities)
            )
        )
