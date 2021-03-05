class SkipRope:
    def partners(self, candidates, height):
        return sorted(
            sorted(
                sorted(candidates, reverse=True),
                cmp=lambda a, b: abs(a - height) - abs(b - height),
            )[:2]
        )
