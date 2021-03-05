class OptimalList:
    def optimize(self, inst):
        d = {}
        for i in inst:
            d[i] = d.get(i, 0) + 1
        s = ""
        s += "E" * max(0, d.get("E", 0) - d.get("W", 0))
        s += "N" * max(0, d.get("N", 0) - d.get("S", 0))
        s += "S" * max(0, d.get("S", 0) - d.get("N", 0))
        s += "W" * max(0, d.get("W", 0) - d.get("E", 0))
        return s
