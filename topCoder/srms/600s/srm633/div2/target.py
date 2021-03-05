class Target:
    def draw(self, n):
        ls, p, wall = [], n / 2, ("#", " ")

        def middle(i, r=1):
            return ("#" + wall[i % 2])[::r] if i != p else ""

        for i in xrange(n):
            j = (n / 2 - abs(n / 2 - i)) / 2
            s = "# " * j + middle(i)
            s += wall[i % 2] * (n - 2 * len(s))
            s += middle(i, -1) + " #" * j
            ls.append(s)
        return ls
